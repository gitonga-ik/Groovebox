from django import forms
from django.db.models import Q
from .models import Song, Playlist


class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "genre", "album"]

class PlaylistCreationForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["title"]

class PlaylistUpdateForm(forms.ModelForm):
    songs = forms.ModelMultipleChoiceField(
        queryset = Song.objects.none(), 
        widget = forms.CheckboxSelectMultiple,
        required = False,
        label = "Select Songs"
    )

    class Meta:
        model = Playlist
        fields = ["title", "songs"]

    def __init__(self, *args, **kwargs):
        query = kwargs.pop("query", None)
        super().__init__(*args, **kwargs)

        queryset = Song.objects.all()
        if query:
            queryset.filter(
                Q(title__icontains=query)|Q(genre__icontains=query)
            )
        self.fields['songs'].queryset = queryset
