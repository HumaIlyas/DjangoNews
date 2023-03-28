from django.test import TestCase, RequestFactory
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from .models import Category, Post, Comment
from .forms import CommentForm
from .views import PostList, PostDetail, PostLike, PostCategory, CommentList, CategoryList


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
        self.assertFalse('news/index.html' in test_response.context)


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
        self.assertFalse('news/post_detail.html' in test_response.context)


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
