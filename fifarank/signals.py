from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from fifarank.models import Match, UserRating

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserRating.objects.create(user=instance)

@receiver(post_save, sender=Match)
def update_user_rating(sender, instance, created, **kwargs):
    if created:
        print(instance)
        print(instance.homeUser.rating)
        print(instance.awayUser.rating)
