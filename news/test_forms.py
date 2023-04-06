from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_comment_body_is_required(self):
        form = CommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['comment'])