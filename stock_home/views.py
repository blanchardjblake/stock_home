"""Define views (URLS)."""
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from stock_home.forms import (
    CompanyCreateUpdateForm,
    PositionCreateUpdateForm,
    TransactionCreateUpdateForm,
)
from stock_home.models import Company, Position, Transaction


# -------------------------------------------------- LANDING
class LandingPageView(generic.TemplateView):
    """Landing page class."""

    template_name = "pages/landing_page.html"


# -------------------------------------------------- LEARNING
class LearningPageView(generic.TemplateView):
    """Learning page class."""

    template_name = "pages/learning_page.html"


# -------------------------------------------------- FORECAST
class ForecastPageView(generic.TemplateView):
    """Forecast page class."""

    template_name = "pages/forecast_page.html"


# -------------------------------------------------- COMPANIES
class CompanyListView(generic.ListView):
    """Company List class."""

    model = Company
    template_name = "stock_home/company/company_list.html"


class CompanyDetailView(generic.DetailView):
    """Company Detail class."""

    model = Company
    template_name = "stock_home/company/company_detail.html"


class CompanyCreateView(generic.CreateView):
    """Company create view."""

    form_class = CompanyCreateUpdateForm
    template_name = "stock_home/generic_create_update.html"
    success_url = reverse_lazy("stock_home:company_list")
    extra_context = {"title_text": "Create Company", "button_text": "Create"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not staff, redirect."""
        if not request.user.is_staff:
            return redirect("stock_home:company_list")
        return super().get(request, *args, **kwargs)


class CompanyUpdateView(generic.UpdateView):
    """Company update view."""

    model = Company
    form_class = CompanyCreateUpdateForm
    template_name = "stock_home/generic_create_update.html"
    success_url = reverse_lazy("stock_home:company_list")
    extra_context = {"title_text": "Update Company", "button_text": "Update"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not staff, redirect."""
        if not request.user.is_staff:
            return redirect("stock_home:company_list")
        return super().get(request, *args, **kwargs)


class CompanyDeleteView(generic.DeleteView):
    """Company delete view."""

    model = Company
    template_name = "stock_home/company/company_delete.html"
    success_url = reverse_lazy("stock_home:company_list")

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not staff, redirect."""
        if not request.user.is_staff:
            return redirect("stock_home:company_list")
        return super().get(request, *args, **kwargs)


# -------------------------------------------------- POSITIONS
class PositionListView(LoginRequiredMixin, generic.ListView):
    """Position List class."""

    model = Position
    template_name = "stock_home/position/position_list.html"

    def get_queryset(self) -> list:
        """Return a list with objects created by current user."""
        return Position.objects.filter(user=self.request.user)


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    """Position Detail class."""

    model = Position
    template_name = "stock_home/position/position_detail.html"

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect."""
        if self.get_object().user != self.request.user:
            return redirect("stock_home:position_list")
        return super().get(request, *args, **kwargs)


class PositionCreateView(generic.CreateView):
    """Position create view."""

    form_class = PositionCreateUpdateForm
    template_name = "stock_home/generic_create_update.html"
    success_url = reverse_lazy("stock_home:position_list")
    extra_context = {"title_text": "Create Position", "button_text": "Create"}

    def form_valid(self, form: object) -> object:
        """When the form submitted is valid, add current user to the form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class PositionUpdateView(generic.UpdateView):
    """Position update view."""

    model = Position
    form_class = PositionCreateUpdateForm
    template_name = "stock_home/generic_create_update.html"
    success_url = reverse_lazy("stock_home:position_list")
    extra_context = {"title_text": "Update Position", "button_text": "Update"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect."""
        if self.get_object().user != self.request.user:
            return redirect("stock_home:position_list")
        return super().get(request, *args, **kwargs)


class PositionDeleteView(generic.DeleteView):
    """Position delete view."""

    model = Position
    template_name = "stock_home/position/position_confirm_delete.html"
    success_url = reverse_lazy("stock_home:position_list")

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect."""
        if self.get_object().user != self.request.user:
            return redirect("stock_home:position_list")
        return super().get(request, *args, **kwargs)


# -------------------------------------------------- TRANSACTIONS
class TransactionListView(LoginRequiredMixin, generic.ListView):
    """Transaction List class."""

    model = Transaction
    template_name = "stock_home/transaction/transaction_list.html"

    def get_queryset(self) -> list:
        """Return a list with objects created by current user."""
        return Transaction.objects.filter(user=self.request.user)


class TransactionDetailView(LoginRequiredMixin, generic.DetailView):
    """Transaction Detail class."""

    model = Transaction
    template_name = "stock_home/transaction/transaction_detail.html"

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect."""
        if self.get_object().user != self.request.user:
            return redirect("stock_home:transaction_list")
        return super().get(request, *args, **kwargs)


class TransactionCreateView(generic.CreateView):
    """Transaction create view."""

    form_class = TransactionCreateUpdateForm
    template_name = "stock_home/generic_create_update.html"
    success_url = reverse_lazy("stock_home:transaction_list")
    extra_context = {"title_text": "Create Transaction", "button_text": "Create"}

    def form_valid(self, form: object) -> object:
        """When the form submitted is valid, add current user to the form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(generic.UpdateView):
    """Transaction update view."""

    model = Transaction
    form_class = TransactionCreateUpdateForm
    template_name = "stock_home/generic_create_update.html"
    success_url = reverse_lazy("stock_home:transaction_list")
    extra_context = {"title_text": "Update Transaction", "button_text": "Update"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect."""
        if self.get_object().user != self.request.user:
            return redirect("stock_home:transaction_list")
        return super().get(request, *args, **kwargs)


class TransactionDeleteView(generic.DeleteView):
    """Transaction delete view."""

    model = Transaction
    template_name = "stock_home/transaction/transaction_confirm_delete.html"
    success_url = reverse_lazy("stock_home:transaction_list")

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect."""
        if self.get_object().user != self.request.user:
            return redirect("stock_home:transaction_list")
        return super().get(request, *args, **kwargs)


# -------------------------------------------------- TRADING
def getData(request):
    """Get data for stock."""
    template = loader.get_template("pages/trading_page.html")

    API_KEY = "GGphVkaXZMMwG6io9V6jVCKlDM5kYq4N3DBynSul"
    ticker = "TSLA"

    stock_data = requests.get(
        f"https://api.stockdata.org/v1/data/quote?symbols={ticker}&api_token={API_KEY}", timeout=10
    ).json()

    d = stock_data["data"][0]

    context = {
        "ticker": d["ticker"],
        "name": d["name"],
        "exchange": d["exchange_short"],
        "price": d["price"],
        "day_high": d["day_high"],
        "day_low": d["day_low"],
        "day_open": d["day_open"],
        "52_week_high": d["52_week_high"],
        "52_week_low": d["52_week_low"],
        "market_cap": d["market_cap"],
        "previous_close_price": d["previous_close_price"],
        "day_change": d["day_change"],
        "volume": d["volume"],
    }

    return HttpResponse(template.render(context, request))
