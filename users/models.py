"""Accounts models."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """A custom User model.

    Arguments:
    ---------
    AbstractUser : class
        Django's `AbstractUser` class.

    Returns:
    -------
    object:
        `CustomUser` model.

    """

    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        """Get the string representation of the object.

        Returns:
        -------
        str
            The unique identifer of the model, `email`.

        """
        return self.email
