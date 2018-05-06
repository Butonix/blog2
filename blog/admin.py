from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):#removes slug field from django-admin
    exclude = ('slug',)

admin.site.register(Category, CategoryAdmin)#register the class

class PostAdmin(admin.ModelAdmin):#modify our posts in django-admin
    exclude = ('slug',)
    list_display = ('title', 'status', 'category', 'created', 'updated',)#displays columns
    list_filter = ('status',)
    search_fields = ('title', 'body')#search feild in django admin

admin.site.register(Post, PostAdmin)
