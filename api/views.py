from music.models import Song, Playlist
from rest_framework import viewsets, permissions, filters, generics, views, response, status
from rest_framework.authtoken.models import Token
from .serializers import AppUserSerializer, SongSerializer, PlaylistSerializer, ArtistSerializer
from .permissions import SongUpdatePermission, SongCreatePermission, PlaylistUpdatePermission
from django.contrib.auth import authenticate

# Create your views here.
class ListenerRegisterView(generics.CreateAPIView):
    serializer_class = AppUserSerializer

class ArtistRegisterView(generics.CreateAPIView):
    serializer_class = ArtistSerializer

class LoginView(views.APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        print(email, password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return response.Response({'token': token.key}, status=status.HTTP_200_OK)
        return response.Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class RetrieveTokenView(views.APIView):
    def post(self, request):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        return response.Response({'token': token.key})

class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    filter_backends = [filters.SearchFilter]
    filterset_fields = ["genre", "album"]
    search_fields = ["title"]

    def get_permissions(self):
        if self.action in ["retrieve", "list"]:
            permission_classes = [permissions.AllowAny]
        elif self.action == "create":
            permission_classes = [SongCreatePermission]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [SongUpdatePermission]
    
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user)

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def get_permissions(self):
        if self.action in ["retrieve", "list"]:
            permission_classes = [permissions.AllowAny]
        elif self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [PlaylistUpdatePermission]

        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)