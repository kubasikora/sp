from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import BlogPost, BlogComment

class PostListView(ListView):
    queryset = BlogPost.objects.all()
    context_object_name = "posts"
    paginate_by = 5
    template_name = "post/list.html"