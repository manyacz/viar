# Generated by Django 4.1 on 2022-08-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_reserve'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserve',
            options={'ordering': ['title'], 'verbose_name': 'Резервация', 'verbose_name_plural': 'Резервации'},
        ),
        migrations.AddField(
            model_name='rooms',
            name='date_end',
            field=models.DateField(auto_now=True, verbose_name='Занято по'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='date_start',
            field=models.DateField(auto_now=True, verbose_name='Занято с'),
        ),
    ]
