from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/blog-latestposts.html')
def latestposts():
    posts = Post.objects.filter(status=True).order_by('-published_date')[:3]
    return {'posts':posts}


