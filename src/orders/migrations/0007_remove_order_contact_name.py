# Generated by Django 3.2.3 on 2021-07-07 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20210708_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='contact_name',
        ),
    ]