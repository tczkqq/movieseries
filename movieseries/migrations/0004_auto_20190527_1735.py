# Generated by Django 2.2.1 on 2019-05-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieseries', '0003_auto_20181228_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, default='defaults/cover.png', max_length=200, upload_to='covers', verbose_name='Cover'),
        ),
    ]
