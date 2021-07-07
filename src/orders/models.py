from django.db import models
from carts.models import Cart

# Create your models here.
class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        related_name="carts",
        verbose_name="Заказ"
    )

    contact_info=models.TextField(
        verbose_name="Контактная информация"
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