"""Stock Home Models (Entities)."""
from datetime import datetime

from django.db import models
from users.managers import CustomUserManager
from users.models import CustomUser


class Company(models.Model):
    """Return a Company model.

    Arguments:
    ---------
    Model : class
        Django's `Model` class.

    Returns:
    -------
    object:
        Model.

    """

    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Company's name", max_length=30, unique=True)
    symbol = models.CharField("Ticker symbol", max_length=5, unique=True, default="")
    value = models.FloatField(default=0.00, null=True)
    share_price = models.FloatField(default=0.00, null=True)
    curr_day_open = models.FloatField(default=0.00, null=True)
    prev_day_open = models.FloatField(default=0.00, null=True)
    curr_day_high = models.FloatField(default=0.00, null=True)
    curr_day_low = models.FloatField(default=0.00, null=True)
    year_high = models.FloatField(default=0.00, null=True)
    year_low = models.FloatField(default=0.00, null=True)
    div_yield = models.FloatField(default=0.00, null=True)
    volume = models.FloatField(default=0.00, null=True)
    avg_volume = models.FloatField(default=0.00, null=True)

    REQUIRED_FIELDS = [name, share_price, symbol]

    def __str__(self) -> str:
        """Return string representation of the object.

        Returns:
        -------
        str
            The unique identifer of the model, `name`.

        """
        return self.name


class Position(models.Model):
    """Return a Position model.

    Arguments:
    ---------
    Model : class
        Django's `Model` class.

    Returns:
    -------
    object:
        Model.

    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    avg_cost = models.FloatField(default=0.00, null=True)
    p_l = models.FloatField(default=0.00, null=True)

    REQUIRED_FIELDS = [user, company, quantity]

    def __str__(self) -> str:
        """Return string representation of the object.

        Returns:
        -------
        str
            The quantity and company of the position.

        """
        return str(self.quantity) + " " + str(self.company) + " @ " + str(self.avg_cost)


class Transaction(models.Model):
    """Return a Transaction model.

    Arguments:
    ---------
    Model : class
        Django's `Model` class.

    Returns:
    -------
    object:
        Model.

    """

    BUY = "Buy"
    SELL = "Sell"
    transaction_types = [(BUY, "Buy"), (SELL, "Sell")]

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    quantity = models.FloatField(default=0.00, null=True)
    type = models.CharField(max_length=4, choices=transaction_types, default=BUY)
    price = models.FloatField(default=0.00, null=True)
    date = models.DateTimeField(default=datetime(2022, 11, 1))

    REQUIRED_FIELDS = [user, company, quantity]

    def __str__(self) -> str:
        """Return string representation of the object.

        Returns:
        -------
        str
            The quantity and company of the position.

        """
        return str(self.quantity) + " " + str(self.company) + " @ " + str(self.price)
