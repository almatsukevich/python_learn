from django.contrib import admin
from . import models

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cart', 'customer_name', 'customer_phone','contact_info', 'created', 'updated']

admin.site.register(models.Order, OrderAdmin)