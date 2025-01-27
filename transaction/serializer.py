from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.hashers import make_password
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            "id",
            "user_id",
            "state",
            "transaction_type",
            "amount_rial",
            "gold_weight_gram",
            "price_per_gram",
            "note",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "user_id",
            "created_at",
            "updated_at",
        ]

class BuyTransactionSerializer(serializers.Serializer):
    amount_rial = serializers.CharField()


class SellTransactionSerializer(serializers.Serializer):
    gold_weight_gram = serializers.CharField()

