from django.contrib import admin
from .models import Song, Playlist

class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "genre", "album", "uploaded_on")
    list_filter = ("artist", "genre", "uploaded_on")
    search_fields = ( "title", "album")
class PlaylistAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Song, SongAdmin)
admin.site.register(Playlist)