# Generated by Django 5.0.2 on 2024-03-02 15:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("collects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("payment_date", models.DateTimeField(auto_now_add=True)),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Описание платежа", null=True
                    ),
                ),
                (
                    "collect",
                    models.ForeignKey(
                        help_text="Сбор средств",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="collects",
                        to="collects.collect",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
                "ordering": ["-id"],
            },
        ),
    ]
