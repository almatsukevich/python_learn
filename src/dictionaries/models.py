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

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"