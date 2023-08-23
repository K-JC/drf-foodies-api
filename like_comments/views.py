from rest_framework import generics, permissions
from drf_foodies_api.permissions import IsOwnerOrReadOnly
from .models import LikeComment
from .serializers import LikeCommentSerializer


class LikeCommentList(generics.ListCreateAPIView):
    """
    Will list all comment likes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class LikeCommentDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a comment like or delete a comment like
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()
