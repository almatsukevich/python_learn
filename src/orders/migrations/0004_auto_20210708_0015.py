# Generated by Django 3.2.3 on 2021-07-07 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210707_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(max_length=18, verbose_name='Телефон пользователя'),
        ),
    ]
