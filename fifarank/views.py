from django.shortcuts import render
from django.views.generic import ListView, DetailView
from fifarank.models import Team, UserRating

class TeamListView(ListView):
    queryset = Team.objects.all()
    context_object_name = "teams"
    paginate_by = 20
    template_name = "team/list.html"

class TeamDetailView(DetailView):
    model = Team
    context_object_name = "team"
    template_name = "team/detail.html"

class UserRankingList(ListView):
    queryset = UserRating.objects.all()
    context_object_name = "ratings"
    paginate_by = 100
    template_name = "rating/list.html"

class UserRankingDetail(DetailView):
    model = UserRating
    context_object_name = "rating"
    template_name = "rating/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        matches = self.object.user.homeUsers.all() | self.object.user.awayUsers.all() 
        context["matches"] = matches.distinct().order_by("-date")[:10]
        return context
