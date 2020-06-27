from django.contrib import admin
from fifarank.models import *

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
    list_display = ("user", "value")
    search_fields = ("user__username",)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "level", "game")
    list_filter = ("game",)
    search_fields = ("name", "country__name")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "league", "rating", "game")
    list_filter = ("game",)
    search_fields = ("name", "league__name")

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("homeUser", "awayUser", "result", "date")
    search_fields = ("homeUser__username", "awayUser__username")

    def result(self, obj):
        return "{} {} : {} {}".format(obj.homeTeam, obj.resultHome, obj.resultAway, obj.awayTeam)