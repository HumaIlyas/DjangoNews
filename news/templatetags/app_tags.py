from ..models import Post, Comment
from ..views import PostDetail
from django import template
register = template.Library()

@register.filter
def is_available(comments, arg):
    comments=comments.filter(is_available = arg)
    return comments