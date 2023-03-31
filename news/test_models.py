from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post, Comment
import pytz
from unittest import mock
import datetime


class TestCategory(TestCase):
    def test_created_on(self):
        mocked = datetime.datetime(2023, 3, 3, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            category = Category.objects.create(title='test', category='test')
            self.assertEqual(category.created_on, mocked)


class TestPost(TestCase):
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

        self.category = Category.objects.create(
            title='test category',
        )
        self.category.save()

    def test_post(self):
        """
        testing post model
        """
        post = Post.objects.create(
            category=self.category,
            title='Test post',
            slug='test-post',
            author=self.user,
            featured_image='Test image',
            excerpt='Test excerpt',
            content='Test content',
            status=0
        )
        post.likes.add(self.user)
        post.likes.count()
        Category = Post({'category': ''})
        self.assertEqual(str(post.title), 'Test post')
        self.assertEqual(str(post.slug), 'test-post')
        self.assertEqual(str(post.author), 'test user')
        self.assertEqual(str(post.featured_image), 'Test image')
        self.assertEqual(str(post.excerpt), 'Test excerpt')
        self.assertEqual(str(post.content), 'Test content')
        self.assertEqual(int(post.status), 0)
        self.assertEqual(post.likes.first(), self.user)
        self.assertEqual(post.likes.count(), 1)
        
    def test_created_on(self):
        mocked = datetime.datetime(2023, 3, 3, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            post = Post.objects.create(title='Test post', slug='test-post')
            self.assertEqual(post.created_on, mocked)

    def test_updated_on(self):
        mocked = datetime.datetime(2023, 3, 3, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            post = Post.objects.create(title='Test post', slug='test-post')
            self.assertEqual(post.updated_on, mocked)

    def test_ordering_post_metaclass(self):
        post = Post.objects.create(title='Test post', slug='test-post')
        self.assertEqual(post._meta.ordering[0], '-created_on')


class TestComment(TestCase):
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
        
        self.post = Post.objects.create(
            title='test post',
        )
        self.post.save()

    def test_comment(self):
        """
        testing comment model
        """
        comment = Comment.objects.create(
            post=self.post,
            name='Test name',
            email='test@email.com',
            comment='Test comment',
            approved=False
        )
        Post = Comment({'post': ''})
        self.assertEqual(comment.__str__(), f"Comment {comment.comment} by {comment.name}")
        self.assertEqual(str(comment.email), 'test@email.com')
        self.assertEqual(str(comment.approved), 'False')

    def test_created_on(self):
        mocked = datetime.datetime(2023, 3, 3, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            comment = Comment.objects.create(post=self.post)
            self.assertEqual(comment.created_on, mocked)

    def test_ordering_comment_metaclass(self):
        comment = Comment.objects.create(post=self.post)
        self.assertEqual(comment._meta.ordering[0], 'created_on')
