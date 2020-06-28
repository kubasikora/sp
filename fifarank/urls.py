from django.urls import path
from fifarank import views
from django.contrib.auth.decorators import login_required

app_name = "fifarank"

urlpatterns = [
    path("teams", login_required(views.TeamListView.as_view()), name="team_list"),
    path("teams/new", login_required(views.TeamAddView.as_view()), name="team_add"),
    path("teams/<str:pk>", login_required(views.TeamDetailView.as_view()), name="team_detail"),
    path("ranking", login_required(views.UserRankingList.as_view()), name="user_rating_list"),
    path("ranking/<str:pk>", login_required(views.UserRankingDetail.as_view()), name="user_rating_detail")
]