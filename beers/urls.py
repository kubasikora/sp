from django.urls import path
from django.contrib.auth.decorators import login_required
from beers import views

app_name = "beers"

urlpatterns = [
    # main view
    path("", login_required(views.BeerListView.as_view()), name="menu"),
    # loaned beer views
    path("loans", login_required(views.BeerListView.as_view()), name="loan_list"),
    path("loans/new", login_required(views.BeerAddView.as_view()), name="loan_add"),
    path("loaner", login_required(views.LoanerView.as_view()), name="loaner"),
    path("loanee", login_required(views.LoaneeView.as_view()), name="loanee")
]