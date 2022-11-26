"""Accounts app URL Configuration."""
from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("list", views.UserListView.as_view(), name="custom_user_list"),
    path("<int:pk>/", views.UserDetailView.as_view(), name="custom_user_detail"),
    path("<int:pk>/update/", views.UserUpdateView.as_view(), name="custom_user_update"),
    path("<int:pk>/delete/", views.UserDeleteView.as_view(), name="custom_user_confirm_delete"),
]
