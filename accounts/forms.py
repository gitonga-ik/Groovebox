from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser, Artist, Profile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ["username", "email"]

class ArtistRegistrationForm(UserCreationForm):
    class Meta:
        model = Artist
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = ["bio", "date_of_birth", "profile_photo"]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
