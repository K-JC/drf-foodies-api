from rest_framework import generics, permissions
from drf_foodies_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    Will list all likes and create a like if user is authenticated
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete a like
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
