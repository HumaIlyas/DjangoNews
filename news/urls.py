from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("comments/", views.CommentList.as_view(), name="comments"),
    path("categories/", views.CategoryList.as_view(), name="categories"),
    
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
