from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=True)
    
    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(status=True, category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 3)
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
    return render(request, 'blog/blog-home.html', {'posts': posts})


def blog_single(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message submited sucsessfully')    
        else:
            messages.error(request, 'Your message did not submited')
    post =  get_object_or_404(Post, pk=pk, status=True)
    comments = Comment.objects.filter(post=post, approved=1)
    form = CommentForm()
    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    posts=Post.objects.filter(status=True)
    if request.method == 'GET':
        if s := request.GET.get('q'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)




