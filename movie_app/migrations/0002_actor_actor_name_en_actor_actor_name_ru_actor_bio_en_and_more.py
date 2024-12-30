# Generated by Django 5.1.4 on 2024-12-18 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='actor_name_en',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='actor_name_ru',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='bio_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='bio_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='country_name_en',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='country',
            name='country_name_ru',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='director',
            name='bio_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='bio_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='director_name_en',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='director_name_ru',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='genre_name_en',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='genre_name_ru',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_name_en',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_name_ru',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='FavouriteMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.favourite')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.movie')),
            ],
        ),
    ]
