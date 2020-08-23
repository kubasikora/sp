from django.urls import path
from blog import views
from django.contrib.auth.decorators import login_required

app_name = "blog"

urlpatterns = [
    # post views
    path("", login_required(views.PostListView.as_view()), name="home"),
    path("post/<str:pk>", login_required(views.PostDetailView.as_view()), name="post_detail")
]