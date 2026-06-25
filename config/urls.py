from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


def health_check(request):
    """
    Simple health endpoint used by:
    - Railway
    - Frontend developers
    - Monitoring tools
    """
    return JsonResponse(
        {
            "status": "healthy",
            "service": "Life Church Limuru API",
            "version": "1.0.0",
        }
    )


urlpatterns = [
    # Health Check
    path("", health_check),

    # Django Admin
    path("admin/", admin.site.urls),

    # ==========================
    # Authentication APIs
    # ==========================
    path(
        "api/auth/",
        include("accounts.urls"),
    ),

    # ==========================
    # Member APIs
    # ==========================
    path(
        "api/members/",
        include("members.urls"),
    ),

    # ==========================
    # API Documentation
    # ==========================
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema",
        ),
        name="swagger-ui",
    ),
    
    path(
    "api/dashboard/",
    include("dashboard.urls"),
),
    
    path(
    "api/church/",
    include("church_groups.urls"),
),
]