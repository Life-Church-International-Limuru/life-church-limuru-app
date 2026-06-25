"""
Dashboard Views
"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import Member
from .services import build_dashboard


class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        member = Member.objects.get(
            user=request.user
        )

        return Response(
            build_dashboard(member)
        )