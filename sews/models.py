from django.db import models
from django.contrib.auth.models import User

class AssetType(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Nazwa")

    def __str__(self):
        return f"{self.name}"

class Asset(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assets", verbose_name="Kupujący")
    assetType = models.ForeignKey(AssetType, on_delete=models.CASCADE, related_name="assets", verbose_name="Typ")
    value = models.DecimalField(max_digits=5, decimal_places=2)
    dateOfPurchase = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-dateOfPurchase",)

