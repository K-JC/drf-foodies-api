from rest_framework import serializers
from .models import LikeComment
from django.db import IntegrityError


class LikeCommentSerializer(serializers.ModelSerializer):
    """
    Like model serializer for comment likes
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LikeComment
        fields = ['id', 'created_at', 'owner', 'comment']

    def create(self, validated_data):
        """
        Handles duplicated comment likes by the same user
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
