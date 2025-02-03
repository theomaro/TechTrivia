from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("account:profile")

    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            UserProfile.objects.create(user=user)  # Create a user profile
            login(request, user)
            return redirect("account:profile")
    else:
        form = UserProfileForm()

    return render(request, "account/signup.html", {"form": form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("account:profile")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("account:profile")

    return render(request, "account/signin.html")


def sign_out(request):
    logout(request)
    return redirect("account:sign_in")


def profile(request):
    user = request.user
    if user.is_authenticated:
        profile = UserProfile.objects.get(user=user)
        return render(request, "account/profile.html", {"profile": profile})

    return redirect("account:sign_in")
