from django.contrib.auth.models import User
from fifarank import serializers
from rest_framework import generics
from fifarank import models

class GameList(generics.ListAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer

class GameInstance(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer



class TeamList(generics.ListCreateAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class TeamInstance(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer



class MatchList(generics.ListCreateAPIView):
    queryset = models.Match.objects.all()
    serializer_class = serializers.MatchSerializer

class MatchInstance(generics.RetrieveAPIView):
    queryset = models.Match.objects.all()
    serializer_class = serializers.MatchSerializer



class UserRatingList(generics.ListAPIView):
    queryset = models.UserRating.objects.all()
    serializer_class = serializers.UserRatingSerializer

class UserRatingInstance(generics.RetrieveAPIView):
    queryset = models.UserRating.objects.all()
    serializer_class = serializers.UserRatingSerializer