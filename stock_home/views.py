"""Define views (URLS)."""
from django.urls import reverse_lazy
from django.views import generic
from users.models import CustomUser

from stock_home.forms import (  # CompanyCreateForm,; CompanyUpdateForm,; PositionCreateForm,; PositionUpdateForm,; TransactionCreateForm,; TransactionUpdateForm,
    UserCreateForm,
    UserUpdateForm,
)
from stock_home.models import Company, Position, Transaction


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
    template_name = "stock_home/company_list.html"


class CompanyDetailView(generic.DetailView):
    """Company Detail class."""

    model = Company
    template_name = "stock_home/company_detail.html"


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
