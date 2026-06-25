from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    MinistryViewSet,
    DepartmentViewSet,
    FamilyGroupViewSet,
    LifeStageGroupViewSet,
)

router = DefaultRouter()

router.register(
    "ministries",
    MinistryViewSet,
    basename="ministries",
)

router.register(
    "departments",
    DepartmentViewSet,
    basename="departments",
)

router.register(
    "family-groups",
    FamilyGroupViewSet,
    basename="family-groups",
)

router.register(
    "life-stage-groups",
    LifeStageGroupViewSet,
    basename="life-stage-groups",
)

urlpatterns = [
    path("", include(router.urls)),
]