from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.base import TemplateView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from .models import Category, Post, Comment
from django.contrib.auth.models import User
from .forms import CommentForm


class PostCategory(View):

    def get(self, request, *args, **kwargs):
        queryset = list(Post.objects.filter(category__category=kwargs['category'].title()))
        context = {
            "post_list": queryset
        }
        return render(request, "news/index.html", context)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "news/index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context = {
            "post": post,
            "comments": comments,
            "commented": False,
            "liked": liked,
            "comment_form": CommentForm()
        }
        return render(request, "news/post_detail.html", context)
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        context = {
            "post": post,
            "comments": comments,
            "commented": True,
            "liked": liked,
            "comment_form": CommentForm()
        }
        return render(request, "news/post_detail.html", context)


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('news/post_detail', args=[slug]))


class PostDelete(View):
    
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if request.user.is_superuser or request.user == post.author:
            post.delete() 
        else:
            raise PermissionDenied

        return render(request, "news/index.html")


class CommentApproval(View):
    
   def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.comments.filter(approved=False).exists():
            if request.user.is_superuser:
                return render(request, "news/approve_comment.html")
        else:
            return render(request, 'news/non_approve_comment.html')


class UserProfile(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "news/profile.html")


class UserAdmin(View):
    def get(request):
        if request.user.is_superuser:
            return render(request, "news/admin.html")


class CommentList(generic.ListView):
    model = Comment
    template_name = "news/post_detail.html"


class CategoryList(generic.ListView):
    model = Category
    template_name = "news/index.html"