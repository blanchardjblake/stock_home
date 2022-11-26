"""Forms for accounts app."""
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Registration form."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "account_type"
        )
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.TextInput(attrs={"class": "form-control"}),
            "password2": forms.TextInput(attrs={"class": "form-control"}),
            "account_type": forms.TextInput(attrs={"class": "form-control"}),
        }


class CustomUserChangeForm(forms.ModelForm):
    """User profile change view."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "account_type"
        )
