from rest_framework import serializers
from .models import Comment
from like_comments.models import LikeComment


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment model serializer, adds extra fields
    when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comment_like_id = serializers.SerializerMethodField()
    comment_like_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_comment_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            comment_like = LikeComment.objects.filter(
                owner=user, comment=obj
            ).first()
            return comment_like.id if comment_like else None
            return None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content', 'comment_like_id',
            'comment_like_count'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field, that way we dont have to
    set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
