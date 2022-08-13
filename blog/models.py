from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    content = RichTextUploadingField()
    tags = TaggableManager()
    counted_views = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=0)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pk': self.id})