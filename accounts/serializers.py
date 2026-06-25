"""
Authentication Serializers

Provides serializers for:

- Member Registration
- Authenticated User Profile

Registration Workflow:
    Create User
            ↓
    Create Pending Member
            ↓
    Await Approval
"""

from django.db import transaction

from rest_framework import serializers

from members.models import Member

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    """
    Register a new church member.

    Creates:
        - User Account
        - Pending Member Record
    """

    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    full_name = serializers.CharField(
        max_length=255
    )

    gender = serializers.ChoiceField(
        choices=Member.GENDER_CHOICES
    )

    date_of_birth = serializers.DateField()

    marital_status = serializers.ChoiceField(
        choices=Member.MARITAL_STATUS_CHOICES
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "phone_number",
            "password",
            "full_name",
            "gender",
            "date_of_birth",
            "marital_status",
        ]

    def validate_username(
        self,
        value: str,
    ) -> str:
        """
        Ensure username is unique.
        """

        if User.objects.filter(
            username=value
        ).exists():
            raise serializers.ValidationError(
                "Username already exists."
            )

        return value

    def validate_email(
        self,
        value: str,
    ) -> str:
        """
        Ensure email is unique.
        """

        if value and User.objects.filter(
            email=value
        ).exists():
            raise serializers.ValidationError(
                "Email address already exists."
            )

        return value

    @transaction.atomic
    def create(
        self,
        validated_data,
    ):
        """
        Create user and pending member
        in a single transaction.
        """

        full_name = validated_data.pop(
            "full_name"
        )

        gender = validated_data.pop(
            "gender"
        )

        date_of_birth = validated_data.pop(
            "date_of_birth"
        )

        marital_status = validated_data.pop(
            "marital_status"
        )

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            phone_number=validated_data.get(
                "phone_number"
            ),
            password=validated_data["password"],
        )

        Member.objects.create(
            user=user,
            full_name=full_name,
            phone_number=user.phone_number,
            email=user.email,
            gender=gender,
            date_of_birth=date_of_birth,
            marital_status=marital_status,
            membership_status="PENDING",
            membership_source="DIRECT",
            active=False,
            member_number=None,
        )

        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Authenticated user profile serializer.
    """

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "member_id",
        ]