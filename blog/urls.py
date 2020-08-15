from django.urls import path
from blog import views
from django.contrib.auth.decorators import login_required

app_name = "blog"

urlpatterns = [
    # main view
    path("", login_required(views.PostListView.as_view()), name="home"),
]