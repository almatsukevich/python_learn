# Generated by Django 3.2.3 on 2021-07-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210708_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.TextField(default=1, verbose_name='Имя пользователя'),
            preserve_default=False,
        ),
    ]
