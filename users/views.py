"""Accounts view."""
from django.urls import reverse_lazy
from django.views import generic

from users.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)
from users.models import CustomUser


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


class UserListView(generic.ListView):
    """User List class."""

    model = CustomUser
    template_name = "custom_user_list.html"


class UserDetailView(generic.DetailView):
    """User Detail class."""

    model = CustomUser
    template_name = "custom_user_detail.html"


class UserUpdateView(generic.UpdateView):
    """User update view."""

    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "custom_user_update.html"
    # which page to show upon success
    success_url = reverse_lazy("users:custom_user_list")


class UserDeleteView(generic.DeleteView):
    """<SomeModel> delete view."""

    model = CustomUser
    template_name = "custom_user_confirm_delete.html"
    # which page to show upon success
    success_url = reverse_lazy("users:custom_user_list")
