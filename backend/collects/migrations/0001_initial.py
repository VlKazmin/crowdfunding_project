# Generated by Django 5.0.2 on 2024-02-29 08:06

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Collect",
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
                    "title",
                    models.CharField(
                        help_text="Название группового сбора.",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "occasion",
                    models.CharField(
                        choices=[
                            ("birthday", "День Рождения"),
                            ("wedding", "Свадьба"),
                            ("anniversary", "Годовщина"),
                            ("graduation", "Выпускной"),
                            ("promotion", "Повышение"),
                            ("retirement", "Выход на пенсию"),
                            ("engagement", "Обручение"),
                            ("baby_shower", "Вечеринка в честь будущего ребенка"),
                            ("holiday", "Праздник"),
                        ],
                        help_text="Повод для создания группового сбора.",
                        max_length=20,
                        verbose_name="Повод",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Описание цели и задач группового сбора.",
                        verbose_name="Описание",
                    ),
                ),
                (
                    "planned_amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Сумма, которую планируется собрать для достижения цели.",
                        max_digits=10,
                        verbose_name="Запланированная сумма",
                    ),
                ),
                (
                    "collected_amount",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        help_text="Текущая сумма, которую удалось собрать.",
                        max_digits=10,
                        verbose_name="Собранная сумма",
                    ),
                ),
                (
                    "contributors_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество пожертвований"
                    ),
                ),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True,
                        help_text="Обложка",
                        null=True,
                        upload_to="collect_covers/",
                        verbose_name="Обложка",
                    ),
                ),
                (
                    "end_datetime",
                    models.DateTimeField(
                        help_text="Дата и время, когда групповой сбор завершится.",
                        verbose_name="Дата и время завершения сбора",
                    ),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        populate_from="title",
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Активный"),
                            ("completed", "Завершен"),
                            ("expired", "Истек срок"),
                        ],
                        default="active",
                        help_text="Текущий статус группового сбора.",
                        max_length=20,
                        verbose_name="Статус",
                    ),
                ),
            ],
            options={
                "verbose_name": "Групповой сбор",
                "verbose_name_plural": "Групповые сборы",
            },
        ),
    ]
