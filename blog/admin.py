from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status', 'created_date', 'published_date')
    list_filter = ('status',)
    search_fields = ('title', 'content')
