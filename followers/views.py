from rest_framework import generics, permissions
from drf_foodies_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    Followers list
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)
    

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follow or delete a follow
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
