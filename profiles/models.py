from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model containing all the profile information
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_ntyuaa'
    )

    class Meta:
        """
        Returns the profile instances in reverse
        (recently created will be first)
        """
        ordering = ['-created_at']

        """
        Returns information on profile user
        """

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Function to create profile when a new
    user is created
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
