from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import AppUser, Profile, Artist
from django.contrib.auth.models import Group

@receiver(post_save, sender=AppUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        listener_group, created = Group.objects.get_or_create(name="Listeners")
        instance.groups.add(listener_group)
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Artist)
def create_artist_profile(sender, instance, created, **kwargs):
    if created:
        artist_group, created = Group.objects.get_or_create(name="Artists")
        instance.groups.add(artist_group)
        Profile.objects.create(user=instance)
