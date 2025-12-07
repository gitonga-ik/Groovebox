from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser, Artist, Profile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ["username", "email"]

    def save(self, commit=True):
        user = super().save()

        if commit:
            Profile.objects.create(user=user)
            
        return user
    

class ArtistRegistrationForm(UserCreationForm):
    class Meta:
        model = Artist
        fields = ["username", "email"]

    def save(self, commit=True):
        user = super().save(commit=False)

        user.role = "Artist"

        if commit:
            user.save()
            Profile.objects.create(user=user)
        
        return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "date_of_birth", "profile_photo"]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
