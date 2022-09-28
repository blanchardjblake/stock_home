"""Tests for users app."""
from http import HTTPStatus

import pytest
from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized

from users.models import CustomUser


class UserManagerTestCase(TestCase):
    """Test `CustomUserManager` class."""

    def test_create_normal(self):
        """Test `create_user` function."""
        user = CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(str(user), "jdoe@gmail.com")

        with pytest.raises(ValueError) as exc_info:
            user = CustomUser.objects.create_user(email=None, password=None)
        self.assertEqual(exc_info.type, ValueError)

    def test_create_superuser(self):
        """Test `create_superuser` function."""
        user = CustomUser.objects.create_superuser(email="jdoe@gmail.com", password="password123")
        self.assertTrue(isinstance(user, CustomUser))

        with pytest.raises(ValueError) as exc_info:
            user = CustomUser.objects.create_superuser(
                email="jdoe1@gmail.com",
                password="password123",
                is_staff=False,
            )
        self.assertEqual(exc_info.type, ValueError)

        with pytest.raises(ValueError) as exc_info:
            user = CustomUser.objects.create_superuser(
                email="jdoe1@gmail.com",
                password="password123",
                is_superuser=False,
            )
        self.assertEqual(exc_info.type, ValueError)


class CustomUserTestCase(TestCase):
    """Tests for `CustomeUser` model."""

    def test_create_user(self):
        """Test to check if `CustomUser` create method is working."""
        user = CustomUser.objects.create(email="jdoe@gmail.com", password="password123")
        query = CustomUser.objects.get(email="jdoe@gmail.com")
        self.assertEqual(user, query)

    def test_create_user_rasies_not_unique_integrity_error_with_same_email(self):
        """Test to check if `CustomUser` create method raises Integrity error."""
        CustomUser.objects.create(email="jdoe@gmail.com", password="password123")

        with pytest.raises(IntegrityError) as exc_info:
            CustomUser.objects.create(email="jdoe@gmail.com", password="password123")
        self.assertEqual(exc_info.type, IntegrityError)


class SignUpViewTestCase(TestCase):
    """Tests for `SignUpView` view."""

    def setUp(self):
        """Set up test data for the class."""
        self.signup_url = reverse("users:signup")

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
        """Test sign up view for strong and weak passwords.

        Registration is successful with strong passwords.
        It fails while registering with weak passwords.

        """
        response = self.client.post(self.signup_url, data=params)
        self.assertEqual(response.status_code, status_code)


class LoginTestCase(TestCase):
    """Tests for `Login` view."""

    def setUp(self):
        """Set up test data for the class."""
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="p@$$W0RDL@rG3")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.login_params = {"username": "jdoe@gmail.com", "password": "p@$$W0RDL@rG3"}

    def test_signinview(self):
        """Test `SignUpView`, it should redirect."""
        response = self.client.post(self.login_url, data=self.login_params)
        # redirects after a successful login
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        response = self.client.get(reverse("home"))
        self.assertEqual(str(response.context.get("user")), "jdoe@gmail.com")

    def test_logged_in_uses_correct_template(self):
        """Test if logged in user sees the about page and user is set correctly."""
        response = self.client.login(email="jdoe@gmail.com", password="p@$$W0RDL@rG3")
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "about.html")

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
        """Test logout by login in first and then logout."""
        response = self.client.post(self.login_url, data=self.login_params)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        response = self.client.get(reverse("home"))
        self.assertEqual(str(response.context.get("user")), "jdoe@gmail.com")

        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(str(response.context.get("user")), "AnonymousUser")
