from django.contrib import admin
from .models import *


@admin.register(Post)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['message', 'created', 'user']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
