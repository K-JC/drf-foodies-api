from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model which is related to the 'owner',
    a user instance. A default image set to always
    reference image.url
    """
    class Category(models.TextChoices):
        """
        Category class which contains choices of
        a category for a post
        """
        CAKES = 'Cakes',
        COOKIES = 'Cookies',
        TARTS = 'Tarts',
        CUPCAKES = 'Cupcakes',
        DOUGHNUTS = 'Doughnuts',
        PIES = 'Pies',
        HOLIDAYS = 'Holidays',
        SCONES = 'Scones',
        PASTRIES = 'Pastries',
        OTHER = 'Other',

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.CharField(
        max_length=50,
        choices=Category.choices
    )
    image = models.ImageField(
        upload_to='images/', default='../default_image_v7fh2u',
        blank=True
    )

    class Meta:
        """
        Orders posts in order of newest to oldest
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns the string of a model instance
        """
        return f'{self.id} {self.title}'
