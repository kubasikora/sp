from django.urls import path
from sews import views
from django.contrib.auth.decorators import login_required

app_name = "sews"

urlpatterns = [
    # main view
    path("", login_required(views.AssetListView.as_view()), name="menu"),
    # asset list
    path("assets", login_required(views.AssetListView.as_view()), name="asset_list"),
    path("assets/new", login_required(views.AssetAddView.as_view()), name="asset_add"),
    # asset types
    path("assets/types/", login_required(views.AssetTypeListView.as_view()), name="assetType_list")
]   