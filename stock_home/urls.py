"""Urls of stock_home."""

from django.urls import path

from stock_home import views

app_name = "stock_home"

urlpatterns = [
    path("users", views.UserListView.as_view(), name="custom_user_list"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="custom_user_detail"),
    path("users/create/", views.UserCreateView.as_view(), name="custom_user_create"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="custom_user_update"),
    path(
        "users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="custom_user_confirm_delete"
    ),
    path("company", views.CompanyListView.as_view(), name="company_list"),
    path("company/read/<int:pk>/", views.CompanyDetailView.as_view(), name="company_detail"),
    path("company/create/", views.CompanyCreateView.as_view(), name="company_create"),
    path("company/update/<int:pk>/", views.CompanyUpdateView.as_view(), name="company_update"),
    path("company/delete/<int:pk>/", views.CompanyDeleteView.as_view(), name="company_delete"),
    path("positions", views.PositionListView.as_view(), name="position_list"),
    path("positions/<int:pk>/", views.PositionDetailView.as_view(), name="position_detail"),
    path("transactions", views.TransactionListView.as_view(), name="transaction_list"),
    path(
        "transactions/<int:pk>/", views.TransactionDetailView.as_view(), name="transaction_detail"
    ),
]
