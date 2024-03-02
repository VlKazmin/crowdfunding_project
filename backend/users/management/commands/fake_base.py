from faker import Faker

import random

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.utils.timezone import make_aware

from collects.models import Collect
from collects.texts import OCCASION_CHOICES
from payments.models import Payment
from users.models import CustomUser

QUANITY = 10


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Очистка базы.",
        )

    def handle(self, *args, **options):
        clear = options["clear"]

        if clear:
            self.clear_database()
        else:
            self.clear_database()
            self.populate_users()
            self.populate_collects()
            self.populate_payments()

    def populate_users(self):
        faker = Faker()

        superuser_username = "admin"
        superuser_email = "admin@admin.com"
        superuser_password = "admin"

        try:
            get_user_model().objects.create_superuser(
                username=superuser_username,
                email=superuser_email,
                password=superuser_password,
            )
            self.stdout.write(self.style.SUCCESS("Суперпользователь создан."))
        except IntegrityError:
            pass

        self.stdout.write(self.style.SUCCESS("Пользователи созданы."))

        for _ in range(QUANITY):
            try:

                username = faker.user_name()
                email = faker.email()
                first_name = faker.first_name()
                last_name = faker.last_name()
                password = faker.password()
                CustomUser.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
            except IntegrityError:
                pass

        self.stdout.write(self.style.SUCCESS("Пользователи созданы."))

    def populate_collects(self):
        faker = Faker()
        users = CustomUser.objects.all()
        occasions = [choice[0] for choice in OCCASION_CHOICES]

        for _ in range(QUANITY):
            try:
                author = random.choice(users)
                title = faker.catch_phrase()
                occasion = random.choice(occasions)
                description = faker.text()
                planned_amount = round(random.uniform(100, 300), 2)
                end_datetime = faker.future_datetime()

                Collect.objects.create(
                    author=author,
                    title=title,
                    occasion=occasion,
                    description=description,
                    planned_amount=planned_amount,
                    end_datetime=make_aware(end_datetime),
                )

            except IntegrityError:
                pass

        self.stdout.write(self.style.SUCCESS("Пожертвования созданы."))

    def populate_payments(self):
        faker = Faker()

        users = CustomUser.objects.all()
        collects = Collect.objects.all()

        for _ in range(QUANITY):
            try:
                user = random.choice(users)
                collect = random.choice(collects)
                amount = round(random.uniform(50, 100), 2)
                description = faker.text()

                if amount <= collect.left_to_collect():
                    Payment.objects.create(
                        user=user,
                        collect=collect,
                        amount=amount,
                        description=description,
                    )

            except IntegrityError:
                pass

        self.stdout.write(self.style.SUCCESS("Платежи созданы."))

    def clear_database(self):
        call_command("flush", "--noinput")
        self.stdout.write(self.style.SUCCESS("База очищена."))
