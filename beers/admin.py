from django.contrib import admin
from beers.models import *

@admin.register(LoanedBeer)
class LoanedBeerAdmin(admin.ModelAdmin):
    list_display = ("loaner", "loanee", "date", "is_given_back")
    search_fields = ("loaner__username", "loanee__username")
