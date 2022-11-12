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

    IA = "Inidvidual"
    FA = "Foreign Citizen"
    UT = "US Trust"
    FT = "Foreign Trust"
    UC = "US Corporation"
    FC = "Foreign Corporation"
    PC = "Partnership/Limited Liability Company"
    MF = "Managed Futures"
    account_types = [
        (IA, "Individual"),
        (FA, "Foreign Citizen"),
        (UT, "US Trust"),
        (FT, "Foreign Trust"),
        (UC, "US Corporation"),
        (FC, "Foreign Corpoartion"),
        (PC, "Partnership/Limited Liability Company"),
        (MF, "Managed Futures"),
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, default="John Doe")
    email = models.EmailField(unique=True)
    password = models.CharField("User's password", max_length=88)
    buying_power = models.FloatField(default=0)
    account_value = models.FloatField(default=0)
    account_type = models.CharField(max_length=37, choices=account_types, default=IA)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        """Return string representation of the object.

        Returns:
        -------
        str
            The unique identifer of the model, `email`.

        """
        return self.email
