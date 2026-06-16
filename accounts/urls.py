from django.urls import path
from .views import RegisterView, MeView

urlpatterns = [
    # Account creation endpoint.
    path("register/", RegisterView.as_view(), name="register"),
    # Authenticated user's profile endpoint.
    path("me/", MeView.as_view(), name="me"),
]
