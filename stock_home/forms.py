"""Forms for Stock Home app."""
from django.forms import ModelForm

from stock_home.models import Company, Position, Transaction
from users.models import CustomUser


# -------------------------------------------------- COMPANIES
class CompanyCreateForm(ModelForm):
    """Company creation form."""

    class Meta:
        """Meta class."""

        model = Company
        fields = (
            "name",
            "symbol",
            "value",
            "share_price",
            "div_yield",
        )


class CompanyUpdateForm(ModelForm):
    """Company update form."""

    class Meta:
        """Meta class."""

        model = Company
        fields = (
            "name",
            "symbol",
            "value",
            "share_price",
            "div_yield",
        )


# -------------------------------------------------- USERS
class UserCreateForm(ModelForm):
    """User creation form."""

    class Meta:
        """Meta class."""

        model = CustomUser
        # list of fields to be used in the form.
        fields = ("name", "email", "password", "account_type")


class UserUpdateForm(ModelForm):
    """User update form."""

    class Meta:
        """Meta class."""

        model = CustomUser
        # list of fields to be used in the form.
        fields = ("name", "email", "password", "account_type")


# -------------------------------------------------- POSITIONS
# For fields, include: user, company, quantity
class PositionCreateForm(ModelForm):
    """Position creation form."""

    class Meta:
        """Meta class."""

        model = Position
        # list of fields to be used in the form.
        fields = ("user", "company", "quantity")


class PositionUpdateForm(ModelForm):
    """Position update form."""

    class Meta:
        """Meta class."""

        model = Position
        # list of fields to be used in the form.
        fields = ("user", "company", "quantity")


# -------------------------------------------------- TRANSACTIONS
# For fields, include: user, company, quantity, type, price, date
class TransactionCreateForm(ModelForm):
    """Transaction creation form."""

    class Meta:
        """Meta class."""

        model = Transaction
        # list of fields to be used in the form.
        fields = ("user", "company", "quantity", "type", "price", "date")


class TransactionUpdateForm(ModelForm):
    """Transaction update form."""

    class Meta:
        """Meta class."""

        model = Transaction
        # list of fields to be used in the form.
        fields = ("user", "company", "quantity", "type", "price", "date")
