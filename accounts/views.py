"""
Authentication Views

Provides endpoints for:

- Member Registration
- Current Authenticated User Profile

Registration Workflow:
    User Registration
            ↓
    Create User Account
            ↓
    Create Pending Member Record
            ↓
    Await Admin Approval
            ↓
    Membership Number Generated
            ↓
    Active Member
"""

from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .models import User
from .serializers import (
    RegisterSerializer,
    UserSerializer,
)


class RegisterView(generics.CreateAPIView):
    """
    Register a new church member.

    Creates:
        - User Account
        - Pending Member Record

    A membership number is NOT generated
    during registration.

    Membership numbers are issued only
    after administrator approval.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(
        self,
        request,
        *args,
        **kwargs,
    ):
        """
        Create a new user and pending member.

        Returns a simplified response suitable
        for frontend consumption.
        """

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "message": (
                    "Registration submitted successfully."
                ),
                "membership_status": "PENDING",
                "approval_required": True,
            },
            status=status.HTTP_201_CREATED,
        )


class MeView(generics.RetrieveAPIView):
    """
    Return the currently authenticated user.

    Requires:
        Bearer JWT Token
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Return the currently authenticated user.
        """

        return self.request.user