from django.shortcuts import render
from django.views.generic import ListView
from beers.models import LoanedBeer

class BeerListView(ListView):
    queryset = LoanedBeer.objects.all()
    context_object_name = "beers"
    paginate_by = 50
    template_name = "loaned_beers/list.html"
