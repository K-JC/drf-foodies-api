from rest_framework import generics, permissions
from drf_foodies_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    Retrieve a list of comments
     """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.annotate(
        comment_like_count=Count('like_comments', distinct=True),
    ).order_by('-created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'owner',
        'post'
        ]

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment
    update or delete it if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
