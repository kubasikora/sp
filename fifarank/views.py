from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from fifarank.models import Team, UserRating, Match, League

class FifarankMenuView(TemplateView):
    template_name = "fifarank.html"


class MatchListView(ListView):
    queryset = Match.objects.all()
    context_object_name = "matches"
    paginate_by = 10
    template_name = "match/list.html"


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


class TeamListView(ListView):
    queryset = Team.objects.all()
    context_object_name = "teams"
    paginate_by = 20
    template_name = "team/list.html"

class TeamDetailView(DetailView):
    model = Team
    context_object_name = "team"
    template_name = "team/detail.html"

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
