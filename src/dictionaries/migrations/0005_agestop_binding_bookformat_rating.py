# Generated by Django 3.2.3 on 2021-06-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0004_publusher_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=3, verbose_name='Возрастные ограничения')),
            ],
            options={
                'verbose_name': 'Тип возрастных ограничений',
                'verbose_name_plural': 'Типы возрастных ограничений',
            },
        ),
        migrations.CreateModel(
            name='Binding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=10, verbose_name='Переплет')),
            ],
            options={
                'verbose_name': 'Тип переплета',
                'verbose_name_plural': 'Типы переплета',
            },
        ),
        migrations.CreateModel(
            name='BookFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=15, verbose_name='Формат')),
            ],
            options={
                'verbose_name': 'Тип формата',
                'verbose_name_plural': 'Типы форматов',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.IntegerField(verbose_name='Рейтинг (0 - 10)')),
            ],
            options={
                'verbose_name': 'Значение рейтинга',
                'verbose_name_plural': 'Значения рейтинга',
            },
        ),
    ]