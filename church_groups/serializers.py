"""
Church Structure Serializers

These serializers expose the church structure
to the mobile application.

The endpoints are read-only.
"""

from rest_framework import serializers

from .models import (
    Ministry,
    Department,
    FamilyGroup,
    LifeStageGroup,
)


class MinistrySerializer(serializers.ModelSerializer):
    """Serializer for church ministries."""

    class Meta:
        model = Ministry
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer for church departments."""

    class Meta:
        model = Department
        fields = "__all__"


class FamilyGroupSerializer(serializers.ModelSerializer):
    """Serializer for family groups."""

    class Meta:
        model = FamilyGroup
        fields = "__all__"


class LifeStageGroupSerializer(serializers.ModelSerializer):
    """Serializer for life stage groups."""

    class Meta:
        model = LifeStageGroup
        fields = "__all__"