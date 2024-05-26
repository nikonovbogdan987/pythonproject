# Generated by Django 5.0.1 on 2024-05-25 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=50, verbose_name='Эл.почта')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('password', models.CharField(max_length=20, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'клиента',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='название игры', max_length=35)),
                ('pictures', models.ImageField(help_text='фото игры', upload_to='')),
                ('genres', models.IntegerField(default=0, help_text='1 - PC, 2 - Console')),
                ('description', models.TextField(help_text='описание игры')),
            ],
            options={
                'verbose_name': 'игру',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Дата заказа')),
                ('name_game', models.CharField(max_length=50, verbose_name='Название игры')),
                ('price', models.IntegerField(verbose_name='Цена игры')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.clients')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
