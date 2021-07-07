from django.db import models
from dictionaries.models import Author, BookSeries, BookGenre, Publusher, Binding, BookFormat, AgeStop, Rating

# Create your models here.
class Book(models.Model):
    name = models.CharField(
        verbose_name = "Название книги",
        max_length=70)

    picture = models.ImageField(
        "Фото обложки",
        upload_to='books/'
    )

    unit_price = models.DecimalField(
        verbose_name = "Цена (BYN)",
        max_digits=5,
        decimal_places=2
    )

    author = models.ManyToManyField(
        Author,
    #    on_delete=models.PROTECT,
        related_name='books'
    )
    
    serie = models.ForeignKey(
        BookSeries,
        on_delete=models.PROTECT,
        related_name='books'
    )

    genre = models.ManyToManyField(
        BookGenre,
     #   on_delete=models.PROTECT,
        related_name='books'
    )    

    year = models.IntegerField(
        verbose_name = "Год издания"
    )

    pages = models.IntegerField(
        verbose_name = "Страниц"
    )

    binding = models.ForeignKey(
        Binding,
        on_delete=models.PROTECT,
        verbose_name = "Переплет",
        )

    book_format = models.ForeignKey(
        BookFormat,
        on_delete=models.PROTECT,
        verbose_name = "Формат"
        )

    isbn = models.IntegerField(
        verbose_name = "ISBN",
        default=9783000000000
    )

    weight = models.IntegerField(
        verbose_name = "Вес (гр)"
    )

    age_stop = models.ForeignKey(
        AgeStop,
        on_delete=models.PROTECT,
        verbose_name = "Возрастные ограничения"
        )

    publusher = models.ForeignKey(
        Publusher,
        on_delete=models.PROTECT,
        related_name='books'
    )    

    quantity = models.IntegerField(
        verbose_name = "Количество книг в наличии",
        default=1
    )

    active = models.BooleanField(
        verbose_name = "Активный (доступен для заказа, Да/Нет)",
        default=True
    )

    rating = models.ForeignKey(
        Rating,
        on_delete=models.PROTECT,
        verbose_name = "Рейтинг (0 - 10)"
    )

    created = models.DateTimeField(
        verbose_name = "Дата внесения в каталог",
        auto_now=False,
        auto_now_add=True
    )

    updated = models.DateTimeField(
        verbose_name = "Дата последнего изменения карточки",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self) ->str:
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

