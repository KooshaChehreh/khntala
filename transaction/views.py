
from rest_framework import status  
from rest_framework.response import Response
from django.conf import settings
from users.permissions import IsAuthenticatedWithToken
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from exceptions import *

from users.models import User
from transaction.models import Transaction
from transaction.serializer import TransactionSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticatedWithToken])
def buy(request):
    serializer = TransactionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        user = User.objects.get(id=request.user.id)
        if user.is_suspended():
            raise SuspendedUser
        amount_rial = serializer.validated_data["amount_rial"]
        gold_weight_gram = amount_rial/settings.PRICE_PER_GRAM_RIALS
        created_transaction = Transaction.objects.create(
            user_id=user.id,
            amount_rial=amount_rial,
            gold_weight_gram=gold_weight_gram
        )
        return Response(TransactionSerializer(created_transaction).data, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        raise UserDoesNotExist




