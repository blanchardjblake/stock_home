"""Accounts models."""
from email.policy import default

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """Return a custom User model.

    Arguments:
    ---------
    AbstractUser : class
        Django's `AbstractUser` class.

    Returns:
    -------
    object:
        `CustomUser` model.

    """

    id = models.BigAutoField(primary_key=True)
    name = models.CharField("User's name", max_length=30, default="John Doe")
    email = models.EmailField(unique=True)
    password = models.CharField("User's password", max_length=20)
    buying_power = models.FloatField(default=0)
    account_value = models.FloatField(default=0)
    account_type = [
        ("I", "Individual"),
        ("F", "Foreign Citizen"),
        ("UT", "US Trust"),
        ("FT", "Foreign Trust"),
        ("UC", "US Corporation"),
        ("FC", "Foreign Corpoartion"),
        ("P", "Partnership/Limited Liability Company"),
        ("MF", "Managed Futures"),
    ]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [name, email, password]

    objects = CustomUserManager()

    def __str__(self) -> str:
        """Return string representation of the object.

        Returns:
        -------
        str
            The unique identifer of the model, `name`.

        """
        return self.email
