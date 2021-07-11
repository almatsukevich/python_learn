# Generated by Django 3.2.3 on 2021-06-30 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0003_auto_20210630_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', models.TextField(verbose_name='Контактная информация')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.cart', verbose_name='Заказ')),
            ],
        ),
    ]