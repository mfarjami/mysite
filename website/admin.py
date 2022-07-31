from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    date_hieratchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'email', 'message')

