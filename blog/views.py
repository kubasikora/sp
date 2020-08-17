from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import BlogPost, BlogComment

class PostListView(ListView):
    queryset = BlogPost.objects.all()
    context_object_name = "posts"
    paginate_by = 5
    template_name = "post/list.html"

class PostDetailView(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "post/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = context["post"].comments.order_by("-creation_date").all()
        return context
