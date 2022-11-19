"""Define views (URLS)."""
from django.views import generic
from django.urls import reverse_lazy
from users.models import CustomUser

from stock_home.models import Company, Position, Transaction
from stock_home.forms import CompanyCreateForm, CompanyUpdateForm


# -------------------------------------------------- USERS
class UserListView(generic.ListView):
    """User List class."""

    model = CustomUser
    template_name = "users/custom_user_list.html"


class UserDetailView(generic.DetailView):
    """User Detail class."""

    model = CustomUser
    template_name = "users/custom_user_detail.html"


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


class PositionDetailView(generic.DetailView):
    """Position Detail class."""

    model = Position
    template_name = "stock_home/position_detail.html"


# -------------------------------------------------- TRANSACTIONS
class TransactionListView(generic.ListView):
    """Transaction List class."""

    model = Transaction
    template_name = "stock_home/transaction_list.html"


class TransactionDetailView(generic.DetailView):
    """Transaction Detail class."""

    model = Transaction
    template_name = "stock_home/transaction_detail.html"
