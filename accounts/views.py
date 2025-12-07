from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, ArtistRegistrationForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("music:home")
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})


def artist_register(request):
    if request.method == "POST":
        form = ArtistRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("music:home")
    else:
        form = ArtistRegistrationForm()

    return render(request, "accounts/artist_register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("music:home")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("music:home")


@login_required
def profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile-home", pk=pk)
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, "accounts/profile.html", {"profile": profile, "form": form})
