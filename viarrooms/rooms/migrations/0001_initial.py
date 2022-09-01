# Generated by Django 4.0.6 on 2022-08-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Номер комнаты')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
                'ordering': ['title'],
            },
        ),
    ]