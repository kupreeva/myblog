from django.contrib import admin
from .models import Post, Category, Tag, Like

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Like)
