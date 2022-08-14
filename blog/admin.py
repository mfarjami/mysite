from django.contrib import admin
from .models import Post, Category, Comment
# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'created_date', 'published_date')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content')

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'approved', 'created_date')
    list_filter = ('approved',)
    search_fields = ('name', 'email', 'subject', 'message')

    
admin.site.register(Category)

