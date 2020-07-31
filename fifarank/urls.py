from django.urls import path
from django.conf.urls import url
from fifarank import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from dal import autocomplete
from fifarank.models import League, Team

app_name = "fifarank"

urlpatterns = [
    path("", login_required(views.MatchListView.as_view()), name="menu"),
    # match views
    path("matches/", login_required(views.MatchListView.as_view()), name="match_list"),
    path("matches/new", login_required(views.MatchAddView.as_view()), name="match_add"),
    # league views
    path("leagues/", login_required(views.LeagueListView.as_view()), name="league_list"),
    path("leagues/<str:pk>", login_required(views.LeagueDetailView.as_view()), name="league_detail"), 
    path("leagues/autocomplete/", login_required(views.LeagueLinkedDataAutocompleteView.as_view()), name="league_autocomplete"),
    # team views
    path("teams", login_required(views.TeamListView.as_view()), name="team_list"),
    path("teams/new", login_required(views.TeamAddView.as_view()), name="team_add"),
    path("teams/<str:pk>", login_required(views.TeamDetailView.as_view()), name="team_detail"),
    path("teams/autocomplete/", login_required(views.TeamLinkedDataAutocompleteView.as_view()), name="team_autocomplete"),
    # ranking views
    path("ranking", login_required(views.UserRankingList.as_view()), name="user_rating_list"),
    path("ranking/<str:pk>", login_required(views.UserRankingDetail.as_view()), name="user_rating_detail")
]