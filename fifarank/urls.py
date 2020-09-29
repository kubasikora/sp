from django.urls import path
from fifarank import views
from fifarank import api
from django.contrib.auth.decorators import login_required

app_name = "fifarank"

urlpatterns = [
    # main view
    path("", login_required(views.MatchListView.as_view()), name="menu"),
    # match views
    path("matches/", login_required(views.MatchListView.as_view()), name="match_list"),
    path("matches/new", login_required(views.MatchAddView.as_view()), name="match_add"),
    # league views
    path("leagues/", login_required(views.LeagueListView.as_view()), name="league_list"),
    path("leagues/new", login_required(views.LeagueAddView.as_view()), name="league_add"),    
    path("leagues/<str:pk>", login_required(views.LeagueDetailView.as_view()), name="league_detail"), 
    path("leagues/autocomplete/", login_required(views.LeagueLinkedDataAutocompleteView.as_view()), name="league_autocomplete"),
    # team views
    path("teams", login_required(views.TeamListView.as_view()), name="team_list"),
    path("teams/new", login_required(views.TeamAddView.as_view()), name="team_add"),
    path("teams/<str:pk>", login_required(views.TeamDetailView.as_view()), name="team_detail"),
    path("teams/autocomplete/", login_required(views.TeamLinkedDataAutocompleteView.as_view()), name="team_autocomplete"),
    # ranking views
    path("ranking", login_required(views.UserRankingList.as_view()), name="user_rating_list"),
    path("ranking/<str:pk>", login_required(views.UserRankingDetail.as_view()), name="user_rating_detail"),
    # game views
    path("games", login_required(views.GameListView.as_view()), name="game_list"),
    path("games/<str:pk>", login_required(views.GameDetailView.as_view()), name="game_detail"),
    
    # api views
    path("api/games", login_required(api.GameList.as_view()), name="game_api"),
    path("api/games/<str:pk>", login_required(api.GameInstance.as_view()), name="game_instance_api"),
    
    path("api/teams", login_required(api.TeamList.as_view()), name="team_api"),
    path("api/teams/<str:pk>", login_required(api.TeamInstance.as_view()), name="team_instance_api"),

    path("api/matches", login_required(api.MatchList.as_view()), name="match_list_api"),
    path("api/matches/<str:pk>", login_required(api.MatchInstance.as_view()), name="match_instance_api"),
    
    path("api/ratings", login_required(api.UserRatingList.as_view()), name="ranking_api"),
    path("api/ratings/<str:pk>", login_required(api.UserRatingInstance.as_view()), name="ranking_user_api")
]