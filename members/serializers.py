"""
Member Serializers

Serializers used by the mobile application
to retrieve member information.
"""

from rest_framework import serializers

from .models import Member


class MemberProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the authenticated member profile.
    """

    family_group = serializers.StringRelatedField()
    life_stage_group = serializers.StringRelatedField()

    ministries = serializers.StringRelatedField(
        many=True
    )

    departments = serializers.StringRelatedField(
        many=True
    )

    class Meta:
        model = Member

        fields = [
            "member_number",
            "full_name",
            "phone_number",
            "email",
            "gender",
            "date_of_birth",
            "marital_status",
            "membership_status",
            "family_group",
            "life_stage_group",
            "ministries",
            "departments",
            "date_joined_church",
        ]