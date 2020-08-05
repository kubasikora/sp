from django.views.generic.base import TemplateView
from fifarank.models import Team, UserRating
from dal import autocomplete
from django.contrib.auth.models import User

class HomePageView(TemplateView):
    template_name = "home.html"

class UserLinkedDataAutocompleteView(autocomplete.Select2QuerySetView):
    model = User

    def get_queryset(self):
        qs = User.objects
        userQuery = self.q
        if userQuery:
            qs = qs.filter(username__startswith=userQuery)
        return qs.all()
