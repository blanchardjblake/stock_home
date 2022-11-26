"""Define views (URLS)."""
from django.urls import reverse_lazy
from django.views import generic

from stock_home.forms import (
    CompanyCreateForm,
    CompanyUpdateForm,
    PositionCreateForm,
    PositionUpdateForm,
    TransactionCreateForm,
    TransactionUpdateForm,
)
from stock_home.models import Company, Position, Transaction


# -------------------------------------------------- LANDING
class LandingPageView(generic.TemplateView):
    """Landing page class."""

    template_name = "stock_home/pages/landing_page.html"


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

    form_class = CompanyCreateForm
    template_name = "stock_home/company/company_create.html"
    success_url = reverse_lazy("stock_home:company_list")


class CompanyUpdateView(generic.UpdateView):
    """Company update view."""

    model = Company
    form_class = CompanyUpdateForm
    template_name = "stock_home/company/company_update.html"
    success_url = reverse_lazy("stock_home:company_list")

    def form_valid(self, form: object) -> object:
        """When the form submitted is valid, add current user to the form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class CompanyDeleteView(generic.DeleteView):
    """Company delete view."""

    model = Company
    template_name = "stock_home/company/company_delete.html"
    success_url = reverse_lazy("stock_home:company_list")


# -------------------------------------------------- POSITIONS
class PositionListView(generic.ListView):
    """Position List class."""

    model = Position
    tempate_name = "stock_home/position_list.html"

    def get_queryset(self) -> list:
        """Return a list with objects created by current user."""
        return Position.objects.filter(owner=self.request.user)


class PositionDetailView(generic.DetailView):
    """Position Detail class."""

    model = Position
    template_name = "stock_home/position_detail.html"


class PositionCreateView(generic.CreateView):
    """Position create view."""

    form_class = PositionCreateForm
    template_name = "stock_home/position_create.html"
    success_url = reverse_lazy("stock_home:position_list")

    def form_valid(self, form: object) -> object:
        """When the form submitted is valid, add current user to the form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class PositionUpdateView(generic.UpdateView):
    """Position update view."""

    model = Position
    form_class = PositionUpdateForm
    template_name = "stock_home/position_update.html"
    success_url = reverse_lazy("stock_home:position_list")


class PositionDeleteView(generic.DeleteView):
    """Position delete view."""

    model = Position
    template_name = "stock_home/position_confirm_delete.html"
    success_url = reverse_lazy("stock_home:position_list")


# -------------------------------------------------- TRANSACTIONS
class TransactionListView(generic.ListView):
    """Transaction List class."""

    model = Transaction
    template_name = "stock_home/transaction_list.html"


class TransactionDetailView(generic.DetailView):
    """Transaction Detail class."""

    model = Transaction
    template_name = "stock_home/transaction_detail.html"


class TransactionCreateView(generic.CreateView):
    """Transaction create view."""

    form_class = TransactionCreateForm
    template_name = "stock_home/transaction_create.html"
    success_url = reverse_lazy("stock_home:transaction_list")

    def form_valid(self, form: object) -> object:
        """When the form submitted is valid, add current user to the form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(generic.UpdateView):
    """Transaction update view."""

    model = Transaction
    form_class = TransactionUpdateForm
    template_name = "stock_home/transaction_update.html"
    success_url = reverse_lazy("stock_home:transaction_list")


class TransactionDeleteView(generic.DeleteView):
    """Transaction delete view."""

    model = Transaction
    template_name = "stock_home/transaction_confirm_delete.html"
    success_url = reverse_lazy("stock_home:transaction_list")
