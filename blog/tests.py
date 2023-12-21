"""Module to test blog post behaviour"""

from django.test import TestCase

from .models import Post


# Create your tests here.
class ModelTesting(TestCase):
    """This class is used to test Post model"""

    def setUp(self):
        """Setting up all used data for the test"""
        self.blog = Post.objects.create(
            title="django-title", author="django-author", slug="django-slug"
        )

    def test_post_model(self):
        """Test Post model"""
        self.assertTrue(isinstance(self.blog, Post))
        self.assertEqual(str(self.blog), "django-title")
        # self.assertEqual(self.blog.title, "django-title")
        # self.assertEqual(self.blog.author, "django-author")
        # self.assertEqual(self.blog.slug, "django-slug")
