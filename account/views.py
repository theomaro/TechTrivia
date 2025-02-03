from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.


def sign_up(request):
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
