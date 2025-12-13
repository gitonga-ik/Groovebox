from django.urls import path
from .views import home, SongDetailView, ArtistDetailView, song_creation, SongUpdateView, SongDeleteView, PlaylistDetailView, playlist_creation, PlaylistDeleteView, PlaylistUpdateView

app_name = "music"

urlpatterns =[
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("songs/<int:pk>", SongDetailView.as_view(), name="song-details"),
    path("songs/create", song_creation, name="song-upload"),
    path("songs/update/<int:pk>", SongUpdateView.as_view(), name="song-update"),
    path("songs/delete/<int:pk>", SongDeleteView.as_view(), name="song-delete"),
    path("artists/<int:pk>", ArtistDetailView.as_view(), name="artist-details"),
    path("playlist/<int:pk>", PlaylistDetailView.as_view(), name="playlist-details"),
    path("playlist/create", playlist_creation, name="playlist-create"),
    path("playlist/update/<int:pk>", PlaylistUpdateView.as_view(), name="playlist-update"),
    path("playlist/delete/<int:pk>", PlaylistDeleteView.as_view(), name="playlist-delete"),
]