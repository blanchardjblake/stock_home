"""Forms for Stock Home app."""
from django.forms import ModelForm
from stock_home.models import Company


class CompanyCreateForm(ModelForm):
    """Company creation form."""

    class Meta:
        """Meta class."""

        model = Company
        fields = (
            "name", "symbol", "value", "share_price", "curr_day_open", "prev_day_open",
            "curr_day_high", "curr_day_low", "year_high", "year_low", "div_yield",
            "volume", "avg_volume"
        )


class CompanyUpdateForm(ModelForm):
    """Company update form."""

    class Meta:
        """Meta class."""

        model = Company
        fields = (
            "name", "symbol", "value", "share_price", "curr_day_open", "prev_day_open",
            "curr_day_high", "curr_day_low", "year_high", "year_low", "div_yield",
            "volume", "avg_volume"
        )
