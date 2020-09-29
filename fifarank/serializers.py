from rest_framework import serializers
from django.contrib.auth.models import User
from fifarank import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")
    
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = ["id", "name"]

class LeagueSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    class Meta:
        model = models.League
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    league = LeagueSerializer()

    class Meta:
        model = models.Team
        fields = "__all__"

class MatchSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    homeTeam = TeamSerializer()
    awayTeam = TeamSerializer()

    class Meta:
        model = models.Match
        fields = "__all__"

class UserRatingSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.UserRating
        fields = "__all__"
