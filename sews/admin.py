from django.contrib import admin
from sews.models import *

@admin.register(AssetType)
class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("buyer", "assetType", "value")
    search_fields = ("buyer__username",)