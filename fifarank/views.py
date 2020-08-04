from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.db.models import Count
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse
from fifarank.models import Team, UserRating, Match, League, Game
from fifarank.logic.matchRecord import getUserRecord
from dal import autocomplete


class FifarankMenuView(TemplateView):
    template_name = "fifarank.html"


class MatchListView(ListView):
    queryset = Match.objects.all()
    context_object_name = "matches"
    paginate_by = 10
    template_name = "match/list.html"

class MatchAddView(CreateView):
    class MatchForm(forms.ModelForm):
        class Meta:
            model = Match
            fields = "__all__"
            widgets = {
                "homeTeam": autocomplete.ModelSelect2(url="fifarank:team_autocomplete", forward=("game",)),
                "awayTeam": autocomplete.ModelSelect2(url="fifarank:team_autocomplete", forward=("game",)),
                "homeUser": autocomplete.ModelSelect2(url="fifarank:user_autocomplete"),
                "awayUser": autocomplete.ModelSelect2(url="fifarank:user_autocomplete")
            }

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

class LeagueLinkedDataAutocompleteView(autocomplete.Select2QuerySetView):
    model = League

    def get_queryset(self):
        qs = League.objects
        gameFK = self.forwarded.get('game', None)
        leagueQuery = self.q
        if gameFK:
            qs = qs.filter(game_id=gameFK)
        if leagueQuery:
            qs = qs.filter(name__startswith=leagueQuery)
        return qs.all()

class LeagueAddView(CreateView):
    model = League
    template_name = "league/add.html"
    success_url = "/fifarank/leagues"
    fields = "__all__"


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

class TeamLinkedDataAutocompleteView(autocomplete.Select2QuerySetView):
    model = Team

    def get_queryset(self):
        qs = Team.objects
        gameFK = self.forwarded.get('game', None)
        teamQuery = self.q
        if gameFK:
            qs = qs.filter(game_id=gameFK)
        if teamQuery:
            qs = qs.filter(name__startswith=teamQuery)
        return qs.all()

class TeamAddView(CreateView):
    class TeamForm(forms.ModelForm):
        class Meta:
            model = Team
            fields = "__all__"
            widgets = {
                "league": autocomplete.ModelSelect2(url="fifarank:league_autocomplete", forward=("game",)),
            }

    model = Team
    template_name = "team/add.html"
    form_class = TeamForm
    success_url = "/fifarank/teams"


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
        distinctMatches = matches.distinct()
        context["matches"] = distinctMatches.order_by("-date")[:10]
        context["match_count"] = len(distinctMatches)

        (w,d,l) = getUserRecord(distinctMatches.all(), self.object.user)
        context["user_record"] = f"{w}W - {d}D - {l}L"

        return context

class UserLinkedDataAutocompleteView(autocomplete.Select2QuerySetView):
    model = User

    def get_queryset(self):
        qs = User.objects
        userQuery = self.q
        if userQuery:
            qs = qs.filter(username__startswith=userQuery)
        return qs.all()


class GameListView(ListView):
    queryset = Game.objects.annotate(count=Count("matches")).order_by("-count").all()
    context_object_name = "games"
    template_name = "game/list.html"

class GameDetailView(DetailView):
    model = Game
    context_object_name = "game"
    template_name = "game/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        leagues = self.object.leagues.all()
        context["leagues_count"] = len(leagues)

        teams = self.object.teams.all()
        context["teams_count"] = len(teams)

        matches = self.object.matches.all() 
        context["matches_count"] = len(matches)
        context["last_matches"] = matches.distinct().order_by("-date")[:5]

        return context