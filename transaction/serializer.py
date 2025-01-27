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
            "amount",
            "gold_amount_gr",
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


    # def create(self, validated_data):
    #     validated_data["password"] = Transaction.hash_password(raw_password=validated_data["password"])
    #     user = super().create(validated_data=validated_data)
    #     return user

    # def update(self, instance, validated_data):
    #     if validated_data["password"]:
    #         validated_data["password"] = Transaction.hash_password(raw_password=validated_data["password"])
    #     user = super().update(instance=instance, validated_data=validated_data)
    #     return user

