from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from sews.models import AssetType, Asset

class AssetListView(ListView):
    queryset = Asset.objects.all()
    template_name = "assets/list.html"
    context_object_name = "assets"
    paginate_by = 20