"""Forms for Stock Home app."""
from django.forms import ModelForm
from users.models import CustomUser

from stock_home.models import Company


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
            "curr_day_open",
            "prev_day_open",
            "curr_day_high",
            "curr_day_low",
            "year_high",
            "year_low",
            "div_yield",
            "volume",
            "avg_volume",
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
            "curr_day_open",
            "prev_day_open",
            "curr_day_high",
            "curr_day_low",
            "year_high",
            "year_low",
            "div_yield",
            "volume",
            "avg_volume",
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


# -------------------------------------------------- COMPANIES
# For fields, include: name, symbol, value, share_price, div_yeild


# -------------------------------------------------- POSITIONS
# For fields, include: user, company, quantity


# -------------------------------------------------- TRANSACTIONS
# For fields, include: user, company, quantity, type, price, date
