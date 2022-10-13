"""Manager class."""
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Custom User Manager.

    Custom user model manager where `email` is the unique identifier
    for authentication instead of the Django's default -- `username`.

    """

    def create_user(self, email: str, password: str, **extra_fields) -> object:
        """Create a new user.

        Arguments:
        ---------
        email : str
            Email address.
        password : str
            Password.

        Returns:
        -------
        object
            `CustomUser` object of the new user.

        Raises:
        ------
        ValueError
            When the no `email` is provided.

        """
        if not email:
            raise ValueError(_("Users must have an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str, **extra_fields) -> object:
        """Create a super user.

        Arguments:
        ---------
        email : str
            Email address.
        password : str
            Password.

        Returns:
        -------
        object
            `CustomUser` object of the super user.

        Raises:
        ------
        ValueError
            When the `is_staff` is not set.
        ValueError
            When the `is_superuser` is not set.

        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
