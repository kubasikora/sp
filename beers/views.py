from django.shortcuts import render
from django.views.generic import ListView, CreateView
from beers.models import LoanedBeer
from django import forms
from django.core.exceptions import PermissionDenied
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

class LoanerView(ListView):
    context_object_name = "beers"
    paginate_by = 50
    template_name = "loaner.html"

    def get_queryset(self):
        if self.request.GET.get("beer"):
            beer_to_return = LoanedBeer.objects.get(id=self.request.GET.get("beer"))
            if self.request.user != beer_to_return.loaner:
                raise PermissionDenied("Tylko piwkodawca może zwrócić piwko")

            beer_to_return.is_given_back = True
            beer_to_return.save()
        return LoanedBeer.objects.filter(loaner=self.request.user).order_by("is_given_back","-date")

class LoaneeView(ListView):
    context_object_name = "beers"
    paginate_by = 50
    template_name = "loanee.html"

    def get_queryset(self):
        return LoanedBeer.objects.filter(loanee=self.request.user).order_by("is_given_back","-date")