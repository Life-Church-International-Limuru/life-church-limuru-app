from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    MeView,
)

urlpatterns = [
    # User registration
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),

    # JWT login
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    # JWT refresh
    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # Current user profile
    path(
        "me/",
        MeView.as_view(),
        name="me",
    ),
]