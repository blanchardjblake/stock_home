"""Urls of stock_home."""

from django.urls import path

from stock_home import views

app_name = "stock_home"

urlpatterns = [
    path("users", views.UserListView.as_view(), name="custom_user_list"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="custom_user_detail"),
    path("company", views.CompanyListView.as_view(), name="company_list"),
    path("company/<int:pk>/", views.CompanyDetailView.as_view(), name="company_detail"),
    path("positions", views.PositionListView.as_view(), name="position_list"),
    path("positions/<int:pk>/", views.PositionDetailView.as_view(), name="position_detail"),
    path("transactions", views.TransactionListView.as_view(), name="transaction_list"),
    path(
        "transactions/<int:pk>/", views.TransactionDetailView.as_view(), name="transaction_detail"
    ),
]
