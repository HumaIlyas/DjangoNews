from django.test import TestCase, RequestFactory
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .models import Category, Post, Comment
from .forms import CommentForm
from .views import PostCategory, PostList, PostDetail, PostLike, PostDelete, CommentApproval, UserProfile, UserAdmin

class TestPostCategory(TestCase):
    def test_get(self):
        category = Category.objects.create(title='test', category='test')
        test_response = self.client.get('/category/')
        self.assertEqual('news/index.html' in test_response.context, False)

class TestPostList(TestCase):
    def setUp(self):
        """
        Setup for testing
        """
        self.user = User.objects.create_user(
            username='test user',
            email='test@email.com',
            password='testpass',
        )
        self.user.save()
    
    def test_post_list(self):
        test_response = self.client.get('/posts/')
        self.assertEqual(test_response.status_code, 404, 'created on')
        self.assertTrue(test_response, 'news/index.html')

class TestPostDetail(TestCase):
    def setUp(self):
        """
        Setup for testing
        """
        self.user = User.objects.create_user(
            username='test user',
            email='test@email.com',
            password='testpass',
        )
        self.user.save()

    def test_get(self):
        queryset = Post.objects.filter(status=1)
        test_response = self.client.get(f'/posts/{queryset}')
        self.assertEqual(test_response.status_code, 404)
        self.assertFalse('news/post_detail.html' in test_response.context)

    def test_post(self):
        queryset = Post.objects.filter(status=1)
        test_response = self.client.post(f'/posts/{queryset}')
        self.assertEqual(test_response.status_code, 404)
        self.assertFalse('news/post_detail.html' in test_response.context)

class TestPostLike(TestCase):
    def setUp(self):
        """
        Setup for testing
        """
        self.user = User.objects.create_user(
            username='test user',
            email='test@email.com',
            password='testpass',
        )
        self.user.save()

    def test_post(self):
        test_response = self.client.get('/posts/')
        post = Post.objects.create(title='Test post')
        post.likes.add(self.user)
        self.assertEqual(test_response.status_code, 404)
        self.assertEqual(post.likes.first(), self.user)
        self.assertTrue(test_response, 'news/post_detail.html')

class TestPostDelete(TestCase):
    def setUp(self):
        """
        Setup for testing
        """
        self.user = User.objects.create_user(
            username='test user',
            email='test@email.com',
            password='testpass',
        )
        self.user.save()

    def test_can_delete_post(self):
        post = Post.objects.create(title='Test post')
        test_response = self.client.get('/posts/')
        self.assertEqual(test_response.status_code, 404)
        self.assertEqual(post.delete(), (1, {'news.Post': 1}))
        self.assertTrue(test_response, 'news/post_detail.html')


class TestCommentApproval(TestCase):    
    def test_get(self):
        test_response = self.client.get('/posts/')
        post = Post.objects.create(title='Test post')
        self.assertEqual(test_response.status_code, 404)
        self.assertTrue(test_response, 'news/non_approve_comment.html')
        self.assertTrue(test_response, 'news/approve_comment.html')


class TestUserProfile(TestCase):    
    def test_get(self):
        test_response = self.client.get('/users/')
        user = User.objects.create_user(username='Test user')
        self.assertEqual(test_response.status_code, 404)
        self.assertTrue(test_response, 'news/profile.html')


class TestUserAdmin(TestCase):    
    def test_get(self):
        test_response = self.client.get('/users/')
        user = User.objects.create_user(username='Test user')
        self.assertEqual(test_response.status_code, 404)
        self.assertTrue(test_response, 'news/admin.html')
            

class TestCommentList(TestCase):    
    def test_comment_list(self):
        test_response = self.client.get('/comments/')
        self.assertEqual(test_response.status_code, 404, 'created_on')
        self.assertFalse('news/post_detail.html' in test_response.context)

class TestCategoryList(TestCase):    
    def test_category_list(self):
        test_response = self.client.get('/category/')
        self.assertEqual(test_response.status_code, 404, 'created_on')
        self.assertFalse('news/index.html' in test_response.context)