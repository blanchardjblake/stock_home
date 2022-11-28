# Generated by Django 4.1 on 2022-11-25 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_customuser_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="name",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(default="Doe", max_length=30),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(default="Doe", max_length=30),
        ),
    ]