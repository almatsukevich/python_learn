# Generated by Django 3.2.3 on 2021-06-30 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0005_auto_20210625_0941'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='carts', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
            ],
        ),
        migrations.CreateModel(
            name='BooksInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Количество')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена за шт')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book', verbose_name='Book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='carts.cart', verbose_name='Cart')),
            ],
        ),
    ]
