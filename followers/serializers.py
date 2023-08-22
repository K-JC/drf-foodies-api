from rest_framework import serializers
from .models import Follower
from django.db import IntegrityError


class FollowerSerializer(serializers.ModelSerializer):
    """
    Follow model serializer for following other users
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_at', 'followed', 'followed_name'
        ]

    def create(self, validated_data):
        """
        Handles duplicated follows by the same user
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
