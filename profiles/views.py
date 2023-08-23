from drf_foodies_api.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from .models import Profile
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework import generics, filters


class ProfileList(generics.ListCreateAPIView):
    """
    Lists all the profiles
    """
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)).order_by(
            '-created_at')


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a profile or edit it if you own the profile
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)).order_by(
            '-created_at')
