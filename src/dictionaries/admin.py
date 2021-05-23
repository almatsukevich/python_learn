from django.contrib import admin
from . import models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'desription']

class BookSeriesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'desription']

class BookGenreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'desription']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'desription']

# Register your models here.
admin.site.register(models.Author, AuthorAdmin)

admin.site.register(models.BookSeries, BookSeriesAdmin)

admin.site.register(models.BookGenre, BookGenreAdmin)

admin.site.register(models.Publusher, PublisherAdmin)