import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.timesince import timesince

class LoanedBeer(models.Model):
    loaner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loaners", verbose_name="Piwkodawca")
    loanee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loanees", verbose_name="Piwkobiorca")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Data pożyczki")
    is_given_back = models.BooleanField(default=False, verbose_name="Czy oddane")

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return f"Piwko od {self.loaner} dla {self.loanee}"

    def save(self, *args, **kwargs):
        if self.loanee == self.loaner:
            raise ValidationError("Nie można pożyczać piwek samemu sobie")
        super(LoanedBeer, self).save(*args, **kwargs)

    def period(self):
        if self.is_given_back:
            return 0
        result = datetime.datetime.now(tz=datetime.timezone.utc) - self.date
        return result.total_seconds() / 3600 / 24