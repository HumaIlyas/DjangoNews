from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Post)
