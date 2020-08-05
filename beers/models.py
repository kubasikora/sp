from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LoanedBeer(models.Model):
    loaner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loaners", verbose_name="Pożyczkodawca")
    loanee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loanees", verbose_name="Pożyczkobiorca")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Data pożyczki")
    is_given_back = models.BooleanField(default=False, verbose_name="Czy oddane")

    class Meta:
        ordering = ("-date",)


    def __str__(self):
        return f"Piwko od {self.loaner} dla {self.loanee}"
