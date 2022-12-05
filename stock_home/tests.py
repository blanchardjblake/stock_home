"""Tests."""
from datetime import datetime

import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from stock_home.models import Company, Position, Transaction
from users.models import CustomUser


# ========================================================================= COMPANY
class CompanyTestCase(TestCase):
    """Tests fo `Company` model."""

    def test_create(self):
        """Tests if `Company`'s `create()` method is working using a query."""
        company = Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )
        query = Company.objects.get(name="FakeCompany")
        self.assertEqual(company, query)

    def test_create_company_raises_not_unique_integrity_error_with_same_name(self):
        """Tests if `Company`'s `create()` method raises an integrity error."""
        Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )

        with pytest.raises(IntegrityError) as exc_info:
            Company.objects.create(
                name="FakeCompany",
                symbol="FCM",
                value=10000000,
                share_price=10.00,
                curr_day_open=9.90,
                prev_day_open=9.95,
                curr_day_high=10.10,
                curr_day_low=9.86,
                year_high=14.00,
                year_low=6.72,
                div_yield=0.30,
                volume=34000000,
                avg_volume=30000000,
            )
        self.assertEqual(exc_info.type, IntegrityError)

    def test_create_company_raises_missing_data_integrity_error_with_no_name(self):
        """Tests if `Company`'s `create()` method raises an integrity error."""
        with pytest.raises(IntegrityError) as exc_info:
            Company.objects.create(
                name=None,
                symbol="FCOM",
                value=10000000,
                share_price=10.00,
                curr_day_open=9.90,
                prev_day_open=9.95,
                curr_day_high=10.10,
                curr_day_low=9.86,
                year_high=14.00,
                year_low=6.72,
                div_yield=0.30,
                volume=34000000,
                avg_volume=30000000,
            )
        self.assertEqual(exc_info.type, IntegrityError)

    def test_update(self):
        """Tests if `Company`'s `update()` method is working using a query."""
        Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )

        company = Company.objects.update(
            name="RealCompany",
            symbol="RCOM",
            value=20000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=40000000,
        )

        self.assertEqual(company, 1)

    def test_delete(self):
        """Tests if `Company`'s `delete()` method is working using a query."""
        Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )

        company = Company.objects.filter(name="FakeCompany").delete()

        self.assertEqual(company[0], 1)


# ========================================================================= POSITION
class PositionTestCase(TestCase):
    """Tests fo `Position` model."""

    def test_create(self):
        """Tests if `Position`'s `create()` method is working using a query."""
        user = CustomUser.objects.create(email="jdoe@gmail.com", password="password123")

        company = Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )

        position = Position.objects.create(
            user=user, company=company, quantity=10, avg_cost=5.00, p_l=0,
        )

        query = Position.objects.get(user=user, company=company)
        self.assertEqual(position, query)

    def test_create_position_raises_missing_data_integrity_error_with_no_user_company(self):
        """Tests if `Position`'s `create()` method raises an integrity error."""
        with pytest.raises(IntegrityError) as exc_info:
            Position.objects.create(
                user=None, company=None, quantity=10, avg_cost=5.00, p_l=0,
            )
        self.assertEqual(exc_info.type, IntegrityError)

    def test_update(self):
        """Tests if `Position`'s `create()` method is working using a query."""
        user = CustomUser.objects.create(email="jdoe@gmail.com", password="password123")

        company = Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )

        Position.objects.create(
            user=user, company=company, quantity=10, avg_cost=5.00, p_l=0,
        )

        position = Position.objects.update(
            user=user, company=company, quantity=20, avg_cost=6.00, p_l=-1,
        )

        self.assertEqual(position, 1)

    def test_delete(self):
        """Tests if `Position`'s `delete()` method is working using a query."""
        user = CustomUser.objects.create(email="jdoe@gmail.com", password="password123")

        company = Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )

        Position.objects.create(
            user=user, company=company, quantity=10, avg_cost=5.00, p_l=0,
        )

        position = Position.objects.filter(user=user, company=company).delete()

        self.assertEqual(position[0], 1)


# ========================================================================= TRANSACTION
class TransactionTestCase(TestCase):
    """Tests for `Transaction` model."""

    def test_create(self):
        """Tests if `Transaction`'s `create()` method is working using a query."""
        user = CustomUser.objects.create(email="jdoe@gmail.com", password="password123")

        company = Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )

        transaction = Transaction.objects.create(
            user=user,
            company=company,
            quantity=10,
            type="Buy",
            price=5.00,
            date=datetime(2022, 11, 8),
        )

        query = Transaction.objects.get(user=user, company=company)
        self.assertEqual(transaction, query)

    def test_create_transaction_raises_missing_data_integrity_error_with_no_user_company(self):
        """Tests if `Transaction`'s `create()` method raises an integrity error."""
        with pytest.raises(IntegrityError) as exc_info:
            Transaction.objects.create(
                user=None,
                company=None,
                quantity=None,
                type="Buy",
                price=5.00,
                date=datetime(2022, 11, 8),
            )
        self.assertEqual(exc_info.type, IntegrityError)

    def test_update(self):
        """Tests if `Transaction`'s `update()` method is working using a query."""
        user = CustomUser.objects.create(email="jdoe@gmail.com", password="password123")

        company = Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )

        Transaction.objects.create(
            user=user,
            company=company,
            quantity=10,
            type="Buy",
            price=5.00,
            date=datetime(2022, 11, 8),
        )

        transaction = Transaction.objects.update(
            user=user,
            company=company,
            quantity=20,
            type="Sell",
            price=6.00,
            date=datetime(2022, 11, 8),
        )

        self.assertEqual(transaction, 1)

    def test_delete(self):
        """Tests if `Transaction`'s `delete()` method is working using a query."""
        user = CustomUser.objects.create(email="jdoe@gmail.com", password="password123")

        company = Company.objects.create(
            name="FakeCompany",
            symbol="FCOM",
            value=10000000,
            share_price=10.00,
            curr_day_open=9.90,
            prev_day_open=9.95,
            curr_day_high=10.10,
            curr_day_low=9.86,
            year_high=14.00,
            year_low=6.72,
            div_yield=0.30,
            volume=34000000,
            avg_volume=30000000,
        )

        Transaction.objects.create(
            user=user,
            company=company,
            quantity=10,
            type="Buy",
            price=5.00,
            date=datetime(2022, 11, 8),
        )

        transaction = Transaction.objects.filter(user=user, company=company).delete()

        self.assertEqual(transaction[0], 1)
