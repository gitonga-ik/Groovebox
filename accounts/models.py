from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

# Create your models here.
class AppUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None, **kwargs):
        if email is None or password is None or username is None:
            raise ValueError("Email and password should be provided")

        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

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

    def save(self, *args, **kwargs):
        self.role = "Artist"
        return super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField("accounts.AppUser", on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)

    def __str__(self):
        return f"I am {self.user.username}"
    
    def save(self, *args, **kwargs):
        if self.date_of_birth and self.date_of_birth > timezone.now().date():
            raise Exception("Invalid date of birth")
        return super().save(*args, **kwargs)