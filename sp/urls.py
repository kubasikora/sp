from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from sp import views

urlpatterns = [
    path('', include('blog.urls', namespace="blog")),
    path("user/autocomplete/", login_required(views.UserLinkedDataAutocompleteView.as_view()), name="user_autocomplete"),
    path('admin/', admin.site.urls),
    path('fifarank/', include('fifarank.urls', namespace='fifarank')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('beers/', include('beers.urls', namespace='beers'))
]
