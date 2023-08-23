from django.db import models
from django.contrib.auth.models import User
from posts.models import Comment


class LikeComment(models.Model):
    """
    class model for liking a comment 
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, related_name='like_comments',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'comment']

    def __str__(self):
        return f'{self.owner} has liked your comment: {self.comment}'
