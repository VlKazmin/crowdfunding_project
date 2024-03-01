import decimal

from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from .models import Payment


@receiver(post_save, sender=Payment)
def payment_success_notification(sender, instance, **kwargs):
    user = instance.user
    collect = instance.collect

    subject = "Успешный платеж"
    message = (
        f"Спасибо за ваш платеж в сбор {collect.title}. \n"
        f"Сумма: {instance.amount}. "
    )

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )
    except Exception as e:
        print(f"Error sending email: {e}")


@receiver(post_save, sender=Payment)
def update_collected_amount(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            collect = instance.collect
            left_to_collect = collect.left_to_collect()

            if collect.status not in ["completed", "expired"]:
                if instance.amount <= left_to_collect:
                    collect.collected_amount += decimal.Decimal(
                        str(instance.amount),
                    )
                    collect.save()
                    cache.delete("payment_list")
