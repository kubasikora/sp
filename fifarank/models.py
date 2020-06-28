from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=8, unique=True, verbose_name="Nazwa gry")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"

class TeamRating(models.TextChoices):
    HALF = '0.5', ('0.5')
    ONE = '1.0', ('1.0')
    ONEANDHALF = '1.5', ('1.5')
    TWO = '2.0', ('2.0')
    TWOANDHALF = '2.5', ('2.5')
    THREE = '3.0', ('3.0')
    THREEANDHALF = '3.5', ('3.5')
    FOUR = '4.0', ('4.0')
    FOURANDHALF = '4.5', ('4.5')
    FIVE = '5.0', ('5.0')

class UserRating(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="rating")
    value = models.DecimalField(max_digits=7, decimal_places=2, default=1500)

    class Meta:
        ordering = ("-value",)

    def __str__(self):
        return f"{self.user}: {self.value}"

class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nazwa kraju")
    code = models.CharField(max_length=5, verbose_name="Kod identyfikacyjny")

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Countries"
    
    def __str__(self):
        return f"{self.code}"

class League(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nazwa ligi")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="leagues", verbose_name="Kraj")
    level = models.PositiveIntegerField(verbose_name="Poziom rozgrywkowy")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="leagues", verbose_name="Gra")

    class Meta:
        ordering = ("country", "level")

    def __str__(self):
        return f"{self.name} ({self.country})"

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa drużyny")
    code = models.CharField(max_length=5, verbose_name="Skrót nazwy")
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams", verbose_name="Liga")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="teams", verbose_name="Gra")
    rating = models.CharField(max_length=3, choices=TeamRating.choices, default=TeamRating.THREE, verbose_name="Ranking")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created", "game", "name")

    def __str__(self):
        return f"{self.name} ({self.code})"

    def get_absolute_url(self):
        return reverse('fifarank:team_detail', args=[self.pk])

class Match(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    resultHome = models.PositiveIntegerField(verbose_name="Wynik gospodarzy")
    resultAway = models.PositiveIntegerField(verbose_name="Wynik gości")
    homeTeam = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="homeTeams", verbose_name="Drużyna gospodarzy")
    awayTeam = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="awayTeams", verbose_name="Drużyna gości")
    homeUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name="homeUsers", verbose_name="Gospodarz")
    awayUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name="awayUsers", verbose_name="Gość")

    class Meta:
        ordering = ("-date",)
        verbose_name_plural = "Matches"

    def __str__(self):
        return f"{self.homeUser} vs {self.awayUser} ({self.resultHome}:{self.resultAway})"