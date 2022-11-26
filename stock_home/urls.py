"""Urls of stock_home."""

from django.urls import path

from stock_home import views

app_name = "stock_home"

urlpatterns = [
    path("", views.LandingPageView.as_view(), name="landing_page"),
    path("company", views.CompanyListView.as_view(), name="company_list"),
    path("company/<int:pk>/", views.CompanyDetailView.as_view(), name="company_detail"),
    path("company/create/", views.CompanyCreateView.as_view(), name="company_create"),
    path("company/<int:pk>/update/", views.CompanyUpdateView.as_view(), name="company_update"),
    path("company/<int:pk>/delete/", views.CompanyDeleteView.as_view(), name="company_delete"),
    path("positions", views.PositionListView.as_view(), name="position_list"),
    path("positions/<int:pk>/", views.PositionDetailView.as_view(), name="position_detail"),
    path("positions/create/", views.PositionCreateView.as_view(), name="position_create"),
    path("positions/<int:pk>/update/", views.PositionUpdateView.as_view(), name="position_update"),
    path(
        "positions/<int:pk>/delete/",
        views.PositionDeleteView.as_view(),
        name="position_confirm_delete",
    ),
    path("transactions", views.TransactionListView.as_view(), name="transaction_list"),
    path(
        "transactions/<int:pk>/", views.TransactionDetailView.as_view(), name="transaction_detail"
    ),
    path("transactions/create/", views.TransactionCreateView.as_view(), name="transaction_create"),
    path(
        "transactions/<int:pk>/update/",
        views.TransactionUpdateView.as_view(),
        name="transaction_update",
    ),
    path(
        "transactions/<int:pk>/delete/",
        views.TransactionDeleteView.as_view(),
        name="transaction_confirm_delete",
    ),
]
