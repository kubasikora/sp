from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver

class Game(models.Model):
    name = models.CharField(max_length=8, unique=True)

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

    @receiver(models.signals.post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserRating.objects.create(user=instance)

class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Countries"
    
    def __str__(self):
        return f"{self.code}"

class League(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="leagues")
    level = models.PositiveIntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="leagues")

    class Meta:
        ordering = ("country", "level")

    def __str__(self):
        return f"{self.name} ({self.country})"

class Team(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="teams")
    rating = models.CharField(max_length=3, choices=TeamRating.choices, default=TeamRating.THREE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created", "game", "name")

    def __str__(self):
        return f"{self.name} ({self.code})"

    def get_absolute_url(self):
        return reverse('fifarank:team_detail', args=[self.pk])

class Match(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    resultHome = models.PositiveIntegerField()
    resultAway = models.PositiveIntegerField()
    homeTeam = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="homeTeams")
    awayTeam = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="awayTeams")
    homeUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name="homeUsers")
    awayUser = models.ForeignKey(User, on_delete=models.PROTECT, related_name="awayUsers")

    class Meta:
        ordering = ("-date",)
        verbose_name_plural = "Matches"

    def __str__(self):
        return f"{self.homeUser} vs {self.awayUser} ({self.resultHome}:{self.resultAway})"
