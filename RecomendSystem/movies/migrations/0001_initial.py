# Generated by Django 2.2.3 on 2019-07-03 06:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('rating_count', models.IntegerField(default=0)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='movies.Genre')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
                'ordering': ('title',),
            },
        ),
    ]
