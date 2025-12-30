from rest_framework import serializers
from music.models import Song, Playlist
from accounts.models import AppUser, Artist

class AppUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AppUser
        fields = ("username", "email", "password")

    def create(self, validated_data):
        try:
            email = validated_data.pop("email")
            username = validated_data.pop("username")
            password = validated_data.pop("password")

            user = AppUser.objects.create_user(username=username, email=email, password=password)
            return user

        except KeyError as error:
            raise(f"Username, email and password required. {error.args}")

class ArtistSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Artist
        fields = ("username", "email", "password")

    def create(self, validated_data):
        try:
            email = validated_data.pop("email")
            username = validated_data.pop("username")
            password = validated_data.pop("password")

            user = Artist.objects.create_user(username=username, email=email, password=password)
            return user

        except KeyError as error:
            raise(f"Username, email and password required. {error.args}")

class SongSerializer(serializers.ModelSerializer):
    artist = serializers.ReadOnlyField(source="artist.username")
    class Meta:
        model = Song
        fields = ("id", "title", "genre", "album", "artist")

class PlaylistSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Playlist
        fields = ("id", "creator", "title", "songs")
    
    