"""
Church Structure Views

Read-only APIs exposing church
structure to authenticated members.
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import (
    Ministry,
    Department,
    FamilyGroup,
    LifeStageGroup,
)

from .serializers import (
    MinistrySerializer,
    DepartmentSerializer,
    FamilyGroupSerializer,
    LifeStageGroupSerializer,
)


class MinistryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only Ministry API.
    """

    queryset = Ministry.objects.all().order_by("name")
    serializer_class = MinistrySerializer
    permission_classes = [IsAuthenticated]


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only Department API.
    """

    queryset = Department.objects.all().order_by("name")
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


class FamilyGroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only Family Group API.
    """

    queryset = FamilyGroup.objects.all().order_by("name")
    serializer_class = FamilyGroupSerializer
    permission_classes = [IsAuthenticated]


class LifeStageGroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only Life Stage Group API.
    """

    queryset = LifeStageGroup.objects.all().order_by("name")
    serializer_class = LifeStageGroupSerializer
    permission_classes = [IsAuthenticated]