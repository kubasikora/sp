from django.urls import path
from fifarank import views

app_name = "fifarank"

urlpatterns = [
    path("teams", views.TeamListView.as_view(), name="team_list"),
    path("teams/<str:pk>", views.TeamDetailView.as_view(), name="team_detail"),
    path("ranking", views.UserRankingList.as_view(), name="user_rating_list"),
    path("ranking/<str:pk>", views.UserRankingDetail.as_view(), name="user_rating_detail")
]