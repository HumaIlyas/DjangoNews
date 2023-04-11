from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path("", views.CommentList.as_view(), name='news/post_detail'),
    path('category/<str:category>', views.PostCategory.as_view(), name='category'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='news/post_detail'),
    path('<slug:slug>/', views.PostComment.as_view(), name='comment_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='like_post'),
    path('delete/<slug:slug>', views.PostDelete.as_view(), name='delete_post'),
    path('approve/<slug:slug>', views.CommentApproval.as_view(), name='approve_comment'),
]
