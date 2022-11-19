"""Define views (URLS)."""
from django.urls import reverse_lazy
from django.views import generic

from stock_home.forms import (
    CompanyCreateForm,
    CompanyUpdateForm,
    PositionCreateForm,
    PositionUpdateForm,
    UserCreateForm,
    UserUpdateForm,
)
from stock_home.models import Company, Position, Transaction
from users.models import CustomUser


# -------------------------------------------------- USERS
class UserListView(generic.ListView):
    """User List class."""

    model = CustomUser
    template_name = "users/custom_user_list.html"


class UserDetailView(generic.DetailView):
    """User Detail class."""

    model = CustomUser
    template_name = "users/custom_user_detail.html"


class UserCreateView(generic.CreateView):
    """User create view."""

    form_class = UserCreateForm
    template_name = "users/custom_user_create.html"
    # which page to show upon success
    # replace "home" with one of the names in urls_patterns of urls.py
    success_url = reverse_lazy("stock_home:custom_user_list")


class UserUpdateView(generic.UpdateView):
    """User update view."""

    model = CustomUser
    form_class = UserUpdateForm
    template_name = "users/custom_user_update.html"
    # which page to show upon success
    success_url = reverse_lazy("stock_home:custom_user_list")


class UserDeleteView(generic.DeleteView):
    """<SomeModel> delete view."""

    model = CustomUser
    template_name = "users/custom_user_confirm_delete.html"
    # which page to show upon success
    success_url = reverse_lazy("stock_home:custom_user_list")


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
    tempate_name = "stock_home/positions/position_list.html"


class PositionDetailView(generic.DetailView):
    """Position Detail class."""

    model = Position
    template_name = "stock_home/positions/position_detail.html"


class PositionCreateView(generic.CreateView):
    """Position create view."""

    form_class = PositionCreateForm
    template_name = "stock_home/position/position_create.html"
    success_url = reverse_lazy("stock_home:position_list")


class PositionUpdateView(generic.UpdateView):
    """Position update view."""

    model = Position
    form_class = PositionUpdateForm
    template_name = "stock_home/position/position_update.html"
    success_url = reverse_lazy("stock_home:position_list")


class PositionDeleteView(generic.DeleteView):
    """Position delete view."""

    model = Position
    template_name = "stock_home/position/position_confirm_delete.html"
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
