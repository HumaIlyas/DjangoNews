from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("", views.CommentList.as_view(), name="home"),
    path("", views.CategoryList.as_view(), name="home"),
    path("", views.PostList.as_view(), name="sports"),
    path("", views.CommentList.as_view(), name="sports"),
    path("", views.CategoryList.as_view(), name="sports"),
    path("", views.PostList.as_view(), name="worklife"),
    path("", views.CommentList.as_view(), name="worklife"),
    path("", views.CategoryList.as_view(), name="worklife"),
    path("", views.PostList.as_view(), name="climate"),
    path("", views.CommentList.as_view(), name="climate"),
    path("", views.CategoryList.as_view(), name="climate"),
    path("", views.PostList.as_view(), name="science"),
    path("", views.CommentList.as_view(), name="science"),
    path("", views.CategoryList.as_view(), name="science"),
    path("", views.PostList.as_view(), name="business"),
    path("", views.CommentList.as_view(), name="business"),
    path("", views.CategoryList.as_view(), name="business"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
