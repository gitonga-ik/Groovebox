from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, PlaylistViewSet, ListenerRegisterView, ArtistRegisterView, LoginView, RetrieveTokenView

router = DefaultRouter()

router.register(r"songs", viewset=SongViewSet, basename="songs")
router.register(r"playlists", viewset=PlaylistViewSet, basename="playlists")

urlpatterns = [
    path("listener-register/", ListenerRegisterView.as_view(), name="listener-register"),
    path("artist-register/", ArtistRegisterView.as_view(), name="artist-register"),
    path("login/", LoginView.as_view(), name="login"),
    path("get-token/", RetrieveTokenView.as_view(), name="login")
] + router.urls