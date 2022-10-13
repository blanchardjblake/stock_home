"""Accounts app URL Configuration."""
from django.urls import path

from users.views import SignUpView

app_name = "users"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
