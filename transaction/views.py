
from rest_framework import status  
from rest_framework.response import Response
from django.conf import settings
from users.permissions import IsAuthenticatedWithToken
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes
)
from exceptions import *
from django.db import transaction
from users.models import User
from transaction.models import Transaction
from transaction.serializer import *


@api_view(["POST"])
def buy(request):
    serializer = BuyTransactionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = request.user
    if user.is_suspended():
        raise SuspendedUser
    amount_rial = serializer.validated_data["amount_rial"]
    gold_weight_gram = amount_rial/settings.PRICE_PER_GRAM_RIALS
    with transaction.atomic():
        created_transaction = Transaction.objects.create(
            user_id=user.id,
            transaction_type=Transaction.TRANSACTION_TYPE_BUY,
            amount_rial=amount_rial,
            gold_weight_gram=gold_weight_gram
        )
        user.gold_weight = gold_weight_gram
        user.save()
    return Response(TransactionSerializer(created_transaction).data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def sell(request):
    serializer = SellTransactionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        user = User.objects.get(id=request.user.id)
        if user.is_suspended():
            raise SuspendedUser
        gold_weight_gram = serializer.validated_data["gold_weight_gram"]
        if not user.check_gold_balance():
            raise UnsufficientBalance
        amount_rial = gold_weight_gram * settings.PRICE_PER_GRAM_RIALS
        with transaction.atomic():
            created_transaction = Transaction.objects.create(
                user_id=user.id,
                transaction_type=Transaction.TRANSACTION_TYPE_SELL,
                amount_rial=amount_rial,
                gold_weight_gram=gold_weight_gram
            )
            user.gold_weight -= gold_weight_gram
            user.save()
        return Response(TransactionSerializer(created_transaction).data, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        raise UserDoesNotExist


@api_view(["GET"])
def user_transactions(request):
    queryset = Transaction.objects.filter(user_id=request.user.id)
    serializer = TransactionSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)