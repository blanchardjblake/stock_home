"""Tests for `users` app."""
from http import HTTPStatus

import pytest
from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized

from users.models import CustomUser


class UserManagerTestCase(TestCase):
    """Test for `CustomUserManager` class."""

    def test_create_normal(self):
        """Test `create_user()`.

        Tests if `create_user()` creates a `CustomUser` model object.
        Tests if the `__str__()` of `CustomUser` returns the email address.

        """
        user = CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(str(user), "jdoe@gmail.com")

    def test_create_user_email_none_raises_value_error(self):
        """Test `create_user()`.

        Tests if `create_user()` raises `ValueError` when the `email` is `None`.

        """
        with pytest.raises(ValueError) as exc_info:
            CustomUser.objects.create_user(email=None, password=None)
        self.assertEqual(exc_info.type, ValueError)

    def test_create_superuser(self):
        """Test `create_superuser()`.

        Tests if `create_superuser()` creates a `CustomUser` model object.
        Tests if the `__str__()` of `CustomUser` returns the email address.

        """
        user = CustomUser.objects.create_superuser(email="jdoe@gmail.com", password="password123")
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(str(user), "jdoe@gmail.com")

    def test_create_superuser_raises_value_error_is_staff_false(self):
        """Test for `create_superuser().

        Tests if `create_superuser()` raises `ValueError` when `is_staff` argument
        to the function is set `False`.

        """
        with pytest.raises(ValueError) as exc_info:
            CustomUser.objects.create_superuser(
                email="jdoe1@gmail.com", password="password123", is_staff=False,
            )
        self.assertEqual(exc_info.type, ValueError)

    def test_create_superuser_raises_value_error_is_superuser_false(self):
        """Test for `create_superuser().

        Tests if `create_superuser()` raises `ValueError` when `is_superuser` argument
        to the function is set `False`.

        """
        with pytest.raises(ValueError) as exc_info:
            CustomUser.objects.create_superuser(
                email="jdoe1@gmail.com", password="password123", is_superuser=False,
            )
        self.assertEqual(exc_info.type, ValueError)


class CustomUserTestCase(TestCase):
    """Tests for `CustomeUser` model."""

    def test_create(self):
        """Tests if `CustomUser`'s `create()` method is working using a query."""
        user = CustomUser.objects.create(email="jdoe@gmail.com", password="password123")
        query = CustomUser.objects.get(email="jdoe@gmail.com")
        self.assertEqual(user, query)

    def test_create_user_rasies_not_unique_integrity_error_with_same_email(self):
        """Tests if `CustomUser`'s `create()` method raises an `IntegrityError`."""
        CustomUser.objects.create(email="jdoe@gmail.com", password="password123")

        with pytest.raises(IntegrityError) as exc_info:
            CustomUser.objects.create(email="jdoe@gmail.com", password="password123")
        self.assertEqual(exc_info.type, IntegrityError)


class SignUpViewTestCase(TestCase):
    """Tests for `SignUpView` view."""

    @parameterized.expand(
        [
            (
                {
                    "first_name": "john",
                    "last_name": "doe",
                    "email": "jdoe@gmail.com",
                    "password1": "p@$$W0RDL@rG3",
                    "password2": "p@$$W0RDL@rG3",
                },
                HTTPStatus.FOUND,
            ),
            (
                {
                    "first_name": "john",
                    "last_name": "doe",
                    "email": "jdoe@gmail.com",
                    "password1": "password",
                    "password2": "password",
                },
                HTTPStatus.OK,
            ),
        ]
    )
    def test_signup_view(self, params, status_code):
        """Test `SignUpView` with strong and weak passwords.

        Tests if registration is successful for strong passwords.
        Tests if registration fails for weak passwords.

        """
        signup_url = reverse("users:signup")
        response = self.client.post(signup_url, data=params)
        self.assertEqual(response.status_code, status_code)


class LoginTestCase(TestCase):
    """Tests for Django's built-in `Login` view."""

    def setUp(self):
        """Set up test data for the class."""
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")

        self.login_params = {"username": "jdoe@gmail.com", "password": "p@$$W0RDL@rG3"}
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="p@$$W0RDL@rG3")

    def test_signinview(self):
        """Test `SignUpView`, it should redirect."""
        response = self.client.post(self.login_url, data=self.login_params)
        # redirects after a successful login
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        response = self.client.get(reverse("home"))
        self.assertEqual(str(response.context.get("user")), "jdoe@gmail.com")

    def test_logged_in_user_sees_correct_template(self):
        """Test if logged in user sees the password change page."""
        response = self.client.login(email="jdoe@gmail.com", password="p@$$W0RDL@rG3")
        response = self.client.get(reverse("password_change"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "registration/password_change.html")

    def test_signinview_invalid_user_password(self):
        """Test login by providing invalid user credentials."""
        response = self.client.post(
            self.login_url, data={"username": "jdoe@gmail.com", "password": "password"}
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "registration/login.html")
        self.assertTrue("errors" in response.context)
        self.assertTrue(
            "Please enter a correct email address and password"
            in str(response.context.get("errors"))
        )
        self.assertEqual(str(response.context.get("user")), "AnonymousUser")

    def test_login_and_logout(self):
        """Test logout by login in first and then logout.

        Tests when a user logs out, the `user` object in the `Response` is "AnyonymousUser".

        """
        response = self.client.post(self.login_url, data=self.login_params)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        response = self.client.get(reverse("home"))
        self.assertEqual(str(response.context.get("user")), "jdoe@gmail.com")

        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(str(response.context.get("user")), "AnonymousUser")
