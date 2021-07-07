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


class BindingAdmin(admin.ModelAdmin):
    list_display = ['pk', 'variant']

class BookFormatAdmin(admin.ModelAdmin):
    list_display = ['pk', 'variant']
    
class AgeStopAdmin(admin.ModelAdmin):
    list_display = ['pk', 'variant']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['pk', 'variant']

# Register your models here.
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.BookSeries, BookSeriesAdmin)
admin.site.register(models.BookGenre, BookGenreAdmin)
admin.site.register(models.Publusher, PublisherAdmin)

admin.site.register(models.Binding, BindingAdmin)
admin.site.register(models.BookFormat, BookFormatAdmin)
admin.site.register(models.AgeStop, AgeStopAdmin)
admin.site.register(models.Rating, RatingAdmin)