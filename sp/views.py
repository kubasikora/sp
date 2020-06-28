from django.views.generic.base import TemplateView
from fifarank.models import Team, UserRating

class HomePageView(TemplateView):
    template_name = "home.html"