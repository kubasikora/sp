from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from fifarank.models import Team, UserRating, Match, League
from django import forms
from django_select2 import forms as s2forms
from django.urls import reverse

class FifarankMenuView(TemplateView):
    template_name = "fifarank.html"


class MatchListView(ListView):
    queryset = Match.objects.all()
    context_object_name = "matches"
    paginate_by = 10
    template_name = "match/list.html"

class TeamWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains"
    ]
    empty_label = "Drużyna"

class UserWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "username__icontains"
    ]

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = "__all__"
        widgets = {
            "homeTeam": TeamWidget,
            "awayTeam": TeamWidget,
            "homeUser": UserWidget,
            "awayUser": UserWidget
        }

class MatchAddView(CreateView):
    model = Match
    template_name = "match/add.html"
    form_class = MatchForm
    success_url = "/fifarank/matches"


class LeagueListView(ListView):
    queryset = League.objects.all()
    context_object_name = "leagues"
    template_name = "league/list.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for league in context["object_list"]:
            league.teams_num = len(league.teams.all())
        return context

class LeagueDetailView(DetailView):
    model = League
    context_object_name = "league"
    template_name = "league/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = context["league"].teams.all()
        return context


class TeamListView(ListView):
    queryset = Team.objects.all()
    context_object_name = "teams"
    paginate_by = 20
    template_name = "team/list.html"

class TeamDetailView(DetailView):
    model = Team
    context_object_name = "team"
    template_name = "team/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        matches = self.object.homeTeams.all() | self.object.awayTeams.all() 
        context["matches"] = matches.distinct().order_by("-date")[:10]
        return context

class TeamAddView(CreateView):
    model = Team
    template_name = "team/add.html"
    fields = "__all__"
    
class UserRankingList(ListView):
    queryset = UserRating.objects.all()
    context_object_name = "ratings"
    template_name = "rating/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for idx, league in enumerate(context["object_list"]):
            league.position = idx + 1
        return context

class UserRankingDetail(DetailView):
    model = UserRating
    context_object_name = "rating"
    template_name = "rating/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        matches = self.object.user.homeUsers.all() | self.object.user.awayUsers.all() 
        context["matches"] = matches.distinct().order_by("-date")[:10]
        return context
