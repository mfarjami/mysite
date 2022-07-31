from django.shortcuts import render
from .models import Post
# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(status=True)
    return render(request, 'blog/blog-home.html', {'posts': posts})


def blog_single(request):
        return render(request, 'blog/blog-single.html')
