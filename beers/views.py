from django.shortcuts import render
from django.views.generic import ListView, CreateView
from beers.models import LoanedBeer
from django import forms
from dal import autocomplete

class BeerListView(ListView):
    queryset = LoanedBeer.objects.all()
    context_object_name = "beers"
    paginate_by = 50
    template_name = "loaned_beer/list.html"

class BeerAddView(CreateView):
    class LoanedBeerForm(forms.ModelForm):
        class Meta:
            model = LoanedBeer
            fields = ("loaner", "loanee")
            widgets = {
                "loaner": autocomplete.ModelSelect2(url="user_autocomplete"),
                "loanee": autocomplete.ModelSelect2(url="user_autocomplete")
            }

    model = LoanedBeer
    template_name = "loaned_beer/add.html"
    form_class = LoanedBeerForm
    success_url = "/beers/loans"