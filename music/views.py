from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Song, Playlist
from accounts.models import Artist
from .forms import SongUploadForm, PlaylistCreationForm, PlaylistUpdateForm

# Create your views here.
def home(request):
    songs = Song.objects.all().order_by("-uploaded_on")[:10]
    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(owner=request.user)
    else:
        playlists = None
    return render(request, "music/home.html", {"songs" : songs, "playlists" : playlists})

class SongDetailView(DetailView):
    model = Song
    template_name = "music/song_details.html"

def song_creation(request):
    if request.method == "POST":
        form = SongUploadForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.artist = request.user
            song.save()
            return redirect("accounts:profile-home", pk=request.user.profile.id)
    else:
        form = SongUploadForm()
    return render(request, "music/song_creation.html", {"form": form})

class SongUpdateView(UserPassesTestMixin, UpdateView):
    model = Song
    fields = ["title", "genre", "album"]
    template_name = "music/song_update.html"

    def get_success_url(self):
        return reverse_lazy("music:song-details", kwargs={"pk" : self.object.pk})

    def test_func(self):
        song = self.get_object()            
        return self.request.user.id == song.artist.id
    
class SongDeleteView(UserPassesTestMixin, DeleteView):
    model = Song
    template_name = "music/song_delete.html"

    def get_success_url(self):
        artist = self.object.artist
        return reverse_lazy("accounts:profile-home", kwargs={"pk": artist.profile.id})
    
    def test_func(self):
        song = self.get_object()            
        return self.request.user.id == song.artist.id

class ArtistDetailView(DetailView):
    model = Artist
    template_name = "music/artist_details.html"

def playlist_creation(request):
    if request.method == "POST":
        form = PlaylistCreationForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.owner = request.user
            playlist.save()
            return redirect("music:playlist-details", pk=playlist.id)
    else:
        form = PlaylistCreationForm()

    return render(request, "music/playlist_creation.html", {"form": form})
    
class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = "music/playlist_details.html"

class PlaylistUpdateView(UserPassesTestMixin, UpdateView):
    model = Playlist
    form_class = PlaylistUpdateForm
    template_name = "music/playlist_update.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["query"] = self.request.GET.get("query", None)
        return kwargs
    
    def get_success_url(self):
        playlist = self.object.id
        return reverse_lazy("music:playlist-details", kwargs={"pk": playlist})
    
    def test_func(self):
        playlist = self.get_object()            
        return self.request.user.id == playlist.owner.id

class PlaylistDeleteView(UserPassesTestMixin, DeleteView):
    model = Playlist
    template_name = "music/playlist_delete.html"

    def get_success_url(self):
        owner = self.object.owner
        return reverse_lazy("accounts:profile-home", kwargs={"pk": owner.profile.id})
    
    def test_func(self):
        playlist = self.get_object()            
        return self.request.user.id == playlist.owner.id