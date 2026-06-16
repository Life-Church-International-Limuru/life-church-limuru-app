from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    # Keep the raw password out of API responses.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone_number",
            "password",
        ]

    def create(self, validated_data):
        # Use create_user so Django hashes the password before saving.
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            phone_number=validated_data.get("phone_number"),
            password=validated_data["password"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Safe profile fields returned to the authenticated user.
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "member_id",
        ]
