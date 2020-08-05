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
        number_of_beers = forms.IntegerField(min_value=1, initial=1)
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

    def form_valid(self, form):
        number_of_beers = form.cleaned_data["number_of_beers"] - 1
        form.cleaned_data.pop("number_of_beers")
        for _ in range(number_of_beers):
            self.object = LoanedBeer.objects.create(**form.cleaned_data)

        return super().form_valid(form)