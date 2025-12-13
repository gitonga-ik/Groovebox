from django.db import models
from accounts.models import AppUser

# Create your models here.
class Song(models.Model):
    artist = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    album = models.CharField(max_length=150)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.artist.role != "Artist":
            raise Exception("Only artists can upload music")
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} by {self.artist.username}"

class Playlist(models.Model):
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title