from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from sews.models import AssetType, Asset
from dal import autocomplete
from django import forms
from django.urls import reverse_lazy
from decimal import Decimal

class AssetListView(ListView):
    queryset = Asset.objects.all()
    template_name = "asset/list.html"
    context_object_name = "assets"
    paginate_by = 20

class AssetAddView(CreateView):
    class AssetForm(forms.ModelForm):
        class Meta:
            model = Asset
            fields = ("assetType", "value")

    form_class = AssetForm
    template_name = "asset/add.html"
    success_url = reverse_lazy("sews:asset_list")

    def form_valid(self, form):
        form.instance.buyer = self.request.user
        return super().form_valid(form)

class AssetTypeListView(ListView):
    queryset = AssetType.objects.all()
    template_name = "assetType/list.html"
    content_object_name = "types"

class AssetTypeLinkedDataAutocompleteView(autocomplete.Select2QuerySetView):
    model = AssetType

    def get_queryset(self):
        qs = AssetType.objects
        assetTypeQuery = self.q
        if assetTypeQuery:
            qs = qs.filter(username__startswith=assetTypeQuery)
        return qs.all()