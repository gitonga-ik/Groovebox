from django.urls import path
from .views import register, artist_register, user_login, user_logout, profile

app_name = "accounts"

urlpatterns = [
    path("register/", register, name="user-register"),
    path("register/artist", artist_register, name="artist-register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/<int:pk>", profile, name="profile-home"),
]
