"""Tests."""
import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from stock_home.models import Company


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
