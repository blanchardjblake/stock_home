# Generated by Django 4.1.2 on 2022-11-19 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_home", "0018_alter_transaction_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 19, 13, 18, 57, 446160)
            ),
        ),
    ]
