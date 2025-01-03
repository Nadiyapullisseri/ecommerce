# Generated by Django 5.1.3 on 2024-11-29 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Userlogin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=40)),
                ("password", models.CharField(max_length=40)),
                ("role", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand_name", models.CharField(max_length=40)),
                ("brand_email", models.CharField(max_length=40)),
                ("password", models.CharField(max_length=40)),
                ("mobile_no", models.IntegerField()),
                ("role", models.CharField(max_length=40)),
                (
                    "login_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="maabees.userlogin",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Userregister",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("email", models.CharField(max_length=40)),
                ("password", models.CharField(max_length=40)),
                ("mobile_no", models.IntegerField()),
                ("role", models.CharField(max_length=40)),
                (
                    "login_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="maabees.userlogin",
                    ),
                ),
            ],
        ),
    ]
