"""Forms for accounts app."""
from django import forms
from django.db import transaction
from .models import CustomUser
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)


class CustomUserCreationForm(UserCreationForm):
    """Registration form."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = ("first_name", "last_name", "email",
                  "password1", "password2")
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'password1': forms.TextInput(attrs={"class": "form-control"}),
            'password2': forms.TextInput(attrs={"class": "form-control"}),
        }


class CustomUserChangeForm(UserChangeForm):
    """User profile change view."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = ('email',)


class TeacherSignUpForm(UserCreationForm):
    """Sign up form for Teachers."""

    class Meta(UserCreationForm.Meta):
        """Meta class."""

        model = CustomUser
        fields = ("first_name", "last_name", "email",
                  "password1", "password2")

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'password1': forms.TextInput(attrs={"class": "form-control"}),
            'password2': forms.TextInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        """Overwrite default method."""
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class StudentSignUpForm(UserCreationForm):
    """Sign up form for Students."""

    class Meta(UserCreationForm.Meta):
        """Meta class."""

        model = CustomUser
        fields = ("first_name", "last_name", "email",
                  "password1", "password2")

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'password1': forms.TextInput(attrs={"class": "form-control"}),
            'password2': forms.TextInput(attrs={"class": "form-control"}),
        }

    @transaction.atomic
    def save(self):
        """Overwrite default method."""
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user
