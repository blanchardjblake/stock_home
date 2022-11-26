"""Accounts view."""
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

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


class UserListView(LoginRequiredMixin, generic.ListView):
    """User List class."""

    model = CustomUser
    template_name = "custom_user_list.html"


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    """User Detail class."""

    model = CustomUser
    template_name = "custom_user_detail.html"

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect."""
        if self.get_object() != self.request.user:
            return redirect("users:custom_user_list")
        return super().get(request, *args, **kwargs)


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    """User update view."""

    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "custom_user_update.html"
    # which page to show upon success
    success_url = reverse_lazy("users:custom_user_list")

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect."""
        if self.get_object() != self.request.user:
            return redirect("users:custom_user_list")
        return super().get(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    """<SomeModel> delete view."""

    model = CustomUser
    template_name = "custom_user_confirm_delete.html"
    # which page to show upon success
    success_url = reverse_lazy("users:custom_user_list")

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect."""
        if self.get_object() != self.request.user:
            return redirect("users:custom_user_list")
        return super().get(request, *args, **kwargs)
