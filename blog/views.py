from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(status=True)
    return render(request, 'blog/blog-home.html', {'posts': posts})


def blog_single(request, pk):
    post = get_object_or_404(Post, pk=pk, status=1)
    return render(request, 'blog/blog-single.html', {'post': post})
