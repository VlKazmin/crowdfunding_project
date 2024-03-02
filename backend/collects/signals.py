import os

from datetime import datetime

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
    current_date = datetime.now()
    old_path = settings.EMAIL_FILE_PATH

    new_path = os.path.join(
        settings.EMAIL_FILE_PATH,
        str("Пожертвования_завершены"),
        str(current_date.year),
        str(current_date.month),
        str(current_date.day),
    )

    if instance.status == "completed":
        subject = "Сбор завершен"
        message = f"Сбор '{title}' завершен."

        contributors = instance.contributors.exclude(id=author.id)
        email_list = [author.email for author in contributors] + [author.email]

        try:
            settings.EMAIL_FILE_PATH = new_path
            send_mail(
                subject,
                message,
                "admin@admin.ru",
                email_list,
            )
        except Exception as e:
            print(f"Ошибка отправки сообщения: {e}")
        finally:
            settings.EMAIL_FILE_PATH = old_path


@receiver(post_save, sender=Collect)
def collect_created_notification(sender, instance, created, **kwargs):
    if created:
        author = instance.author
        title = instance.title

        current_date = datetime.now()
        old_path = settings.EMAIL_FILE_PATH
        new_path = os.path.join(
            settings.EMAIL_FILE_PATH,
            str("Пожертвования"),
            str(current_date.year),
            str(current_date.month),
            str(current_date.day),
            str(title),
            author.email,
        )

        subject = "Сбор создан"
        message = f"Сбор '{title}' успешно создан."

        try:
            settings.EMAIL_FILE_PATH = new_path
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [author.email],
            )
        except Exception as e:
            print(f"Error sending email: {e}")
        finally:
            settings.EMAIL_FILE_PATH = old_path
