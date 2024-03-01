from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Collect


@receiver(pre_save, sender=Collect)
def update_collect_status(sender, instance, **kwargs):
    """Проверяем, истек ли срок завершения сбора"""

    if instance.end_datetime <= timezone.now():
        instance.status = "expired"
    elif instance.left_to_collect() == 0:
        instance.status = "completed"
    else:
        instance.status = "active"


@receiver(pre_save, sender=Collect)
def update_slug(sender, instance, **kwargs):
    instance.slug = instance.title


@receiver(post_save, sender=Collect)
def end_collected_notification(sender, instance, **kwargs):
    title = instance.title
    author = instance.author

    if instance.status == "completed":
        subject = "Сбор завершен"
        message = f"Сбор '{title}' завершен."

        contributors = instance.contributors.exclude(id=author.id)
        email_list = [author.email for author in contributors] + [author.email]

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                email_list,
            )
        except Exception as e:
            print(f"Error sending email: {e}")


@receiver(post_save, sender=Collect)
def collect_created_notification(sender, instance, created, **kwargs):
    if created:
        author = instance.author
        title = instance.title

        subject = "Сбор создан"
        message = f"Сбор '{title}' успешно создан."

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [author.email],
            )
        except Exception as e:
            print(f"Error sending email: {e}")
