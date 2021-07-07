from django.contrib import admin
from . import models

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

admin.site.register(models.Book, BookAdmin)