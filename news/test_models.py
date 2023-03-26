from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post, Comment


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
        post_string='Test post'
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

        def test_created_on_auto_now_add_True(self):
            post = Post.objects.create(created_on='Test news Post')
            self.assertTrue(post.created_on)

        def test_updated_on_auto_now_True(self):
            post = Post.objects.create(updated_on='Test news Post')
            self.assertTrue(post.updated_on)

        def test_ordering_are_explicit_in_post_metaclass(self):
            ordering = tilte._meta.ordering
            self.assertEqual(ordering[0], '-created_on')


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
            body='Test body'
        )

        post = Comment.objects.create(
            post=self.post,
        )
        post.comments.add(self.user)
        post.comments.count()
        comment_string = 'Test comment'
        Post = Comment({'post': ''})
        self.assertEqual(str(comment.name), 'Test name')
        self.assertEqual(str(comment.email), 'test@email.com')
        self.assertEqual(str(comment.body), 'Test body')
        self.assertEqual(post.comments.first(), self.user)
        self.assertEqual(post.comments.count(), 1)

        def test_created_on_auto_now_add_True(self):
            comment = Comment.objects.create(created_on='Test news Comment')
            self.assertTrue(comment.created_on)

        def test_approved_defaults_to_false(self):
            comment = Comment.objects.create(comment='Test news Comment')
            self.assertFalse(comment.approved)

        def test_ordering_are_explicit_in_comment_metaclass(self):
            ordering = comments._meta.ordering
            self.assertEqual(ordering[0], 'created_on')
