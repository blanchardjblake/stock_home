# Generated by Django 4.1.2 on 2022-11-11 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "stock_home",
            "0003_alter_company_avg_volume_alter_company_div_yield_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="quantity",
            field=models.FloatField(),
        ),
    ]
