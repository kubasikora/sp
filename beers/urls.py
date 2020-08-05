from django.urls import path
from django.contrib.auth.decorators import login_required
from beers import views

app_name = "beers"

urlpatterns = [
    # main view
    path("", login_required(views.BeerListView.as_view()), name="menu"),
    # loaned beer views
    path("loans", login_required(views.BeerListView.as_view()), name="loan_list"),
    path("loans/new", login_required(views.BeerAddView.as_view()), name="loan_add")
]