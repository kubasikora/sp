from django.contrib import admin
from blog.models import *

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("author", "creation_date")
    search_fields = ("author__username",)

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("author", "creation_date")
    search_fields = ("author__username",)