# Generated by Django 3.2.3 on 2021-07-07 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=18, verbose_name='Телефон'),
        ),
    ]