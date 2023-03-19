from django.test import TestCase
from .models import Category, Post


class TestCategory(TestCase):
    def test_created_on_auto_now_add_True(self):
        category = Category.objects.create(created_on='Test news Category')
        self.assertTrue(category.created_on)

    def test_category_string_method_returns_category(self):
        category = Category.objects.create(category='Test news Category')
        self.assertEqual(str(category), 'Test news Category')
    
    def test_category_string_method_returns_title(self):
        category = Category.objects.create(category='Test news Category')
        self.assertEqual(str(category), 'Test news Category')


class TestPost(TestCase):
    def test_post_string_method_returns_title(self):
        post = Post.objects.create(post='Test news Post')
        self.assertEqual(str(post), 'Test news Post')

    def test_created_on_auto_now_add_True(self):
        post = Post.objects.create(created_on='Test news Post')
        self.assertTrue(post.created_on)

    def test_updated_on_auto_now_True(self):
        post = Post.objects.create(updated_on='Test news Post')
        self.assertTrue(post.updated_on)
