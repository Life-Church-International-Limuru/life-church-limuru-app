"""
Member Views

Provides endpoints related to
church members.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Member
from .serializers import MemberProfileSerializer


class MemberProfileView(generics.RetrieveAPIView):
    """
    Return the profile of the
    currently authenticated member.
    """

    serializer_class = MemberProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Return the Member record
        linked to the authenticated user.
        """

        return Member.objects.get(
            user=self.request.user
        )