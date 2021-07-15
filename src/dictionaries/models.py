from django.db import models

# Create manual "Authors"

class Author(models.Model):
    name = models.CharField(
        verbose_name = "Фамилия.И.О автора",
        max_length=30)

    desription = models.TextField(
        verbose_name = "Об авторе",
        blank=True,
        null=True)
    
    picture = models.ImageField(
        "Изображение",
        upload_to='authors/'
    )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('manuals:author', kwargs={'pk' : self.pk})

    def to_class_name(self):
        return self._meta.verbose_name_plural

    def __str__(self) ->str:
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


# Create manual "Book Series"
class BookSeries(models.Model):
    name = models.CharField(
        verbose_name = "Название серии",
        max_length=30)

    desription = models.TextField(
        verbose_name = "Описание серии",
        blank=True,
        null=True)

    def __str__(self) ->str:
        return self.name
   
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('manuals:bookseries', kwargs={'pk' : self.pk})

    def to_class_name(self):
        return self._meta.verbose_name_plural
    class Meta:
        verbose_name = "Книжная серия"
        verbose_name_plural = "Книжные серии"


# Create manual "Book genre"
class BookGenre(models.Model):
    name = models.CharField(
        verbose_name = "Название жанра",
        max_length=30)

    desription = models.TextField(
        verbose_name = "Описание жанра",
        blank=True,
        null=True)

    def __str__(self) ->str:
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('manuals:bookgenre', kwargs={'pk' : self.pk})

    def to_class_name(self):
        return self._meta.verbose_name_plural
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

        
# Create manual "Publisher"
class Publusher(models.Model):
    name = models.CharField(
        verbose_name = "Название издательства",
        max_length=40)

    desription = models.TextField(
        verbose_name = "Описание издательства",
        blank=True,
        null=True)
    
    picture = models.ImageField(
        "Изображение",
        upload_to='publishers/'
    )

    def __str__(self) ->str:
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('manuals:publisher', kwargs={'pk' : self.pk})

    def to_class_name(self):
        return self._meta.verbose_name_plural
    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

class Binding(models.Model):
    variant = models.CharField(
        verbose_name = "Переплет",
        max_length=10)
    def __str__(self) ->str:
        return self.variant
    class Meta:
        verbose_name = "Тип переплета"
        verbose_name_plural = "Типы переплета"

class BookFormat(models.Model):
    variant = models.CharField(
        verbose_name = "Формат",
        max_length=15)
    def __str__(self) ->str:
        return self.variant
    class Meta:
        verbose_name = "Тип формата"
        verbose_name_plural = "Типы форматов"

class AgeStop(models.Model):
    variant = models.CharField(
        verbose_name = "Возрастные ограничения",
        max_length=3)
    def __str__(self) ->str:
        return self.variant
    class Meta:
        verbose_name = "Тип возрастных ограничений"
        verbose_name_plural = "Типы возрастных ограничений"

class Rating(models.Model):
    variant = models.IntegerField(
        verbose_name = "Рейтинг (0 - 10)")
    def __str__(self) ->str:
        var_str = str(self.variant)
        return var_str
    class Meta:
        verbose_name = "Значение рейтинга"
        verbose_name_plural = "Значения рейтинга"


class Status(models.Model):
    variant = models.CharField(
        verbose_name = "Статус заказа",
        max_length=10)
    def __str__(self) ->str:
        return self.variant
    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказа"


 
