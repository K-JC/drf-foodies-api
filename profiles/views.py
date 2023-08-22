from drf_foodies_api.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import generics


class ProfileList(generics.ListCreateAPIView):
    """
    Lists all the profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a profile or edit it if you own the profile
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
