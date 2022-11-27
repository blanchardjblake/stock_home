"""Forms for Stock Home app."""
from django.forms import ModelForm

from stock_home.models import Company, Position, Transaction
from users.models import CustomUser


# -------------------------------------------------- COMPANIES
class CompanyCreateUpdateForm(ModelForm):
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


# -------------------------------------------------- POSITIONS
# For fields, include: user, company, quantity
class PositionCreateUpdateForm(ModelForm):
    """Position creation form."""

    class Meta:
        """Meta class."""

        model = Position
        # list of fields to be used in the form.
        fields = ("company", "quantity")


# -------------------------------------------------- TRANSACTIONS
# For fields, include: user, company, quantity, type, price, date
class TransactionCreateUpdateForm(ModelForm):
    """Transaction creation form."""

    class Meta:
        """Meta class."""

        model = Transaction
        # list of fields to be used in the form.
        fields = ("company", "quantity", "type", "price", "date")
