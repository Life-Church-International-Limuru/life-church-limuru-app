from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    # Public endpoint for creating a new user account.
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class MeView(generics.RetrieveAPIView):
    # Returns the profile for the currently authenticated JWT user.
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # DRF uses this object when serializing the /me/ response.
        return self.request.user
