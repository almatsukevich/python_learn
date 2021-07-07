from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime    

# Create your models here.
User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="carts",
        verbose_name="Покупатель",
        on_delete=models.PROTECT
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

    @property
    def total_price(self):
        total_price = 0
        goods = self.goods.all()
        for good in goods:
            total_price += good.total_price
        return total_price

class BooksInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name="goods",
        on_delete=models.CASCADE,
        verbose_name="Cart"
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.PROTECT,
        verbose_name="Book"
    )
    quantity = models.IntegerField(
        verbose_name="Количество",
        default=1
    )
    unit_price = models.DecimalField(
        verbose_name="Цена за шт",
        max_digits=5,
        decimal_places=2
    )

    @property
    def total_price(self):
        return self.unit_price * self.quantity