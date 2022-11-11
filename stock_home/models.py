"""Stock Home Models (Entities)."""
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
    value = models.FloatField()
    share_price = models.FloatField()
    curr_day_open = models.FloatField()
    prev_day_open = models.FloatField()
    curr_day_high = models.FloatField()
    corr_day_low = models.FloatField()
    year_high = models.FloatField()
    year_low = models.FloatField()
    div_yield = models.FloatField()
    volume = models.FloatField()
    avg_volume = models.FloatField()

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
    quantity = models.FloatField()
    avg_cost = models.FloatField()
    p_l = models.FloatField()

    REQUIRED_FIELDS = [user, company, quantity, avg_cost]

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

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    quantity = models.FloatField()
    type = [("Buy", "Buy"), ("Sell", "Sell")]
    price = models.FloatField()
    date = models.DateTimeField

    REQUIRED_FIELDS = [user, company, quantity, type, price, date]

    def __str__(self) -> str:
        """Return string representation of the object.

        Returns:
        -------
        str
            The quantity and company of the position.

        """
        return str(self.quantity) + " " + str(self.company) + " @ " + str(self.price)
