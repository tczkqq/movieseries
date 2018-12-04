# Generated by Django 2.1.3 on 2018-11-20 16:29

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('title_translated', models.TextField(blank=True, max_length=200)),
                ('director', models.TextField(max_length=150)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('added', models.DateField(auto_now_add=True)),
                ('movie_year', models.DateField(blank=True)),
                ('cover', models.ImageField(upload_to='')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
