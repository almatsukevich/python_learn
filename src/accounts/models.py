from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name="profile"
        )

    phone = models.CharField(
        verbose_name = "Телефон",
        max_length=15)

    country = models.CharField(
        verbose_name = "Страна",
        max_length=20,
        blank=True,
        null=True)

    city = models.CharField(
        verbose_name = "Город",
        max_length=20,
        blank=True,
        null=True)

    index = models.IntegerField(
        verbose_name = "Индекс",
        blank=True,
        null=True)

    address1 = models.CharField(
        verbose_name = "Адрес1",
        max_length=30,
        blank=True,
        null=True)

    address2 = models.CharField(
        verbose_name = "Адрес2",
        max_length=30,
        blank=True,
        null=True)

    info = models.TextField(
        verbose_name = "Дополнительная информация",
        blank=True,
        null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)