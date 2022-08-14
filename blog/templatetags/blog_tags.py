from django import template
from blog.models import Post, Category, Comment

register = template.Library()

@register.inclusion_tag('blog/blog-latestposts.html')
def latestposts():
    posts = Post.objects.filter(status=True).order_by('-published_date')[:3]
    return {'posts':posts}


@register.inclusion_tag('blog/blog-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}


@register.simple_tag(name='comments_count')
def function(pk):
    return Comment.objects.filter(post=pk, approved=1).count()