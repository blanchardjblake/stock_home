# Generated by Django 4.1.2 on 2022-11-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_home", "0007_rename_corr_day_low_company_curr_day_low"),
    ]

    operations = [
        migrations.AlterField(
            model_name="position", name="avg_cost", field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="position", name="p_l", field=models.FloatField(null=True),
        ),
    ]
