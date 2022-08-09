from pydoc import pager
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
# Create your views here.


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=True)
    
    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(status=True, category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 1)
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
    return render(request, 'blog/blog-home.html', {'posts': posts})


def blog_single(request, pk):
    post = get_object_or_404(Post, pk=pk, status=1)
    return render(request, 'blog/blog-single.html', {'post': post})

def blog_search(request):
    posts=Post.objects.filter(status=True)
    if request.method == 'GET':
        if s := request.GET.get('q'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)