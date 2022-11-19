# Generated by Django 4.1.2 on 2022-11-19 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_home", "0008_alter_position_avg_cost_alter_position_p_l"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="avg_volume",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="curr_day_high",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="curr_day_low",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="curr_day_open",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="div_yield",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="prev_day_open",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="share_price",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="value",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="volume",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="year_high",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="year_low",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="position",
            name="avg_cost",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="position",
            name="p_l",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="position", name="quantity", field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 19, 13, 5, 25, 845752)
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="price",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="quantity",
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
