from django.test import TestCase, RequestFactory
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from .models import Category, Post, Comment
from .forms import CommentForm
from .views import PostList, PostDetail, PostLike, PostCategory, CommentList, CategoryList


class TestPostCategory(TestCase):
    def test_get(self):
        pass


class TestPostList(TestCase):    
    def test_post_list(self):
        pass

class TestPostDetail(TestCase):
    def test_get(self):
        pass

    def test_post(self):
        pass


class TestPostLike(TestCase):
    def test_post(self):
        pass


class TestPostDelete(TestCase):
    def test_get(self):
        pass


class TestCommentList(TestCase):    
    def test_comment_list(self):
        pass


class TestCategoryList(TestCase):    
    def test_category_list(self):
        pass