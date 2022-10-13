"""Accounts view."""
from django.urls import reverse_lazy
from django.views import generic

from users.forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    """User registration view.

    Arguments:
    ---------
    generic : object
        Django generic `CreateView`.

    """

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
