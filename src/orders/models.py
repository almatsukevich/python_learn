from django.db import models
from carts.models import Cart
from dictionaries.models import Status
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        related_name="carts",
        verbose_name="Корзина"
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        default=1,
        verbose_name = "Статус заказа"
    )

    customer_name = models.CharField(
        verbose_name = "Имя пользователя",
        max_length=30,
        )
    
    customer_phone = models.CharField(
        verbose_name = "Телефон пользователя",
        max_length=18,
        )

    contact_info=models.TextField(
        verbose_name="Контактная информация",
        blank=True,
        null=True,
    )

    created = models.DateTimeField(
        verbose_name = "Дата создания",
        auto_now=False,
        auto_now_add=True
    )

    updated = models.DateTimeField(
        verbose_name = "Дата изменения",
        auto_now=True,
        auto_now_add=False
    )

    manager = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name = "Менеджер"
    )