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
    paginate_by = 50

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
    context_object_name = "types"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for item in context["object_list"]:
            item.count = Asset.objects.filter(assetType=item).count()
        return context

class PersonalAssetListView(ListView):
    template_name = "asset/list.html"
    context_object_name = "assets"
    paginate_by = 50

    def get_queryset(self):
        return Asset.objects.filter(buyer=self.request.user).all()

    def sum_expenditure(self, qs):
        total_expenditure = Decimal('0.0')
        for item in qs:
            total_expenditure += item.value
        return total_expenditure

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_personal"] = True
        context["total_expenditure"] = self.sum_expenditure(context["object_list"])
        return context