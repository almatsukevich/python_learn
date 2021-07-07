# Generated by Django 3.2.3 on 2021-07-06 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20210630_1230'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='carts', to='carts.cart', verbose_name='Заказ'),
        ),
    ]
