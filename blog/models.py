"""Blog post model"""
from django.db import models


# Create your models here.
class Post(models.Model):
    """Blog model used to store blog information"""

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f"{self.title}"
