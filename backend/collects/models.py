from autoslug import AutoSlugField

from django.core.validators import MinValueValidator
from django.db import models

from .texts import (
    OCCASION_CHOICES,
    STATUS_CHOICES,
)

from users.models import CustomUser


class Collect(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="collects_authored",
        verbose_name="Автор",
        help_text="Автор группового сбора.",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Название группового сбора.",
        unique=True,
    )
    occasion = models.CharField(
        max_length=20,
        choices=OCCASION_CHOICES,
        verbose_name="Повод",
        help_text="Повод для создания группового сбора.",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание цели и задач группового сбора.",
    )
    planned_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Запланированная сумма",
        help_text="Сумма, которую планируется собрать для достижения цели.",
        validators=[MinValueValidator(0)]
    )
    collected_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Собранная сумма",
        help_text="Текущая сумма, которую удалось собрать.",
    )
    contributors = models.ManyToManyField(
        CustomUser,
        through="payments.Payment",
        related_name="contributions",
        verbose_name="Участники",
        help_text="Пользователи, внесшие свой вклад в групповой сбор.",
    )
    contributors_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество пожертвований",
    )
    cover_image = models.ImageField(
        upload_to="collect_covers/",
        null=True,
        blank=True,
        verbose_name="Обложка",
        help_text="Обложка",
    )
    end_datetime = models.DateTimeField(
        verbose_name="Дата и время завершения сбора",
        help_text="Дата и время, когда групповой сбор завершится.",
    )
    slug = AutoSlugField(
        unique=True,
        populate_from="title",
        verbose_name="Slug",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
        verbose_name="Статус",
        help_text="Текущий статус группового сбора.",
    )

    class Meta:
        verbose_name = "Групповой сбор"
        verbose_name_plural = "Групповые сборы"
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def left_to_collect(self):
        """Возвращает сумму которую осталось собрать."""

        return self.planned_amount - self.collected_amount
