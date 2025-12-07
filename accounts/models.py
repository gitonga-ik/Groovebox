from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class AppUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **kwargs):
        if email is None or password is None:
            raise ValueError("Email and password should be provided")

        normal_email = self.normalize_mail(email)
        user = self.model(email=normal_email, **kwargs)
        user.set_password(password)
        user.save()

    def create_superuser(self, email=None, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_admin", True)
        kwargs.setdefault("role", "Admin")

        return self.create_user(email, password, **kwargs)


class AppUser(AbstractUser):
    ROLES = [("Admin", "Admin"), ("Artist", "Artist"), ("Listener", "Listener")]

    role = models.CharField(max_length=50, choices=ROLES, default="Listener")
    email = models.EmailField(max_length=150, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username}"


class ArtistManager(AppUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="Artist")


class Artist(AppUser):
    objects = ArtistManager()

    class Meta:
        proxy = True


class Profile(models.Model):
    user = models.OneToOneField("accounts.AppUser", on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    bio = models.TextField(null=True)
    profile_photo = models.ImageField(upload_to="profile_pictures/", null=True)

    def __str__(self):
        return f"I am {self.user.username}"
