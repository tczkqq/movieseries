# Generated by Django 2.1.3 on 2018-11-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieseries', '0004_auto_20181122_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers', verbose_name='Okładka'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_year',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Rok produkcji'),
        ),
    ]
