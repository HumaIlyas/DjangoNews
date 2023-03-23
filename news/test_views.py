from django.test import TestCase
from django.test.client import Client
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from .models import Post
from .views import PostList, CommentList


class TestPost(TestCase):
    def setUp(self):
        """
        Setup for testing
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='test user',
            email='test@email.com',
            password='testpass',
        )
        self.user.save()
        login = self.client.login(username='test user', password='testpass')
        self.failUnless(login, 'Could not log in')
    
    def test_post_list(self):
        test_response = self.client.get('/posts/')
        self.assertEqual(test_response.status_code, 404, 'created_on')
        self.assertFalse('post_list' in test_response.context)


class TestComment(TestCase):    
    def test_comment_list(self):
        test_response = self.client.get('/comments/')
        self.assertEqual(test_response.status_code, 200, 'created_on')
        self.assertTrue('comment_list' in test_response.context)


class TestCategory(TestCase):    
    def test_category_list(self):
        test_response = self.client.get('/categories/')
        self.assertEqual(test_response.status_code, 404, 'created_on')
        self.assertFalse('category_list' in test_response.context)
