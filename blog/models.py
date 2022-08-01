from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # category
    content = models.TextField()
    #tag
    #image
    counted_views = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=0)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
