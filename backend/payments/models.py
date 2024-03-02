from django.db import models
from django.core.validators import MinValueValidator

from collects.models import Collect
from users.models import CustomUser


class Payment(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="payments",
        help_text="Пользователь",
    )
    collect = models.ForeignKey(
        to=Collect,
        on_delete=models.CASCADE,
        related_name="collects",
        help_text="Сбор средств",
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    payment_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Описание платежа",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"{self.user.username} - {self.amount}"
