from django.urls import path
from . import views

# configure your app urls here

app_name = "account"

urlpatterns = [
    path("signup/", view=views.sign_up, name="sign_up"),
    path("signin/", view=views.sign_in, name="sign_in"),
    path("profile/", view=views.profile, name="profile"),
]
