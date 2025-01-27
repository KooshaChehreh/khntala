from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "phone",
            "password",
            "gold_weight",
            "created_at",
            "updated_at",
            "suspended_at",
        ]
        read_only_fields = [
            "id",
            "phone",
            "created_at",
            "updated_at",
            "suspended_at",
        ]


    def create(self, validated_data):
        validated_data["password"] = User.hash_password(raw_password=validated_data["password"])
        user = super().create(validated_data=validated_data)
        return user

    def update(self, instance, validated_data):
        if validated_data["password"]:
            validated_data["password"] = User.hash_password(raw_password=validated_data["password"])
        user = super().update(instance=instance, validated_data=validated_data)
        return user