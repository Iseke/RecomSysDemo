# Generated by Django 2.2.3 on 2019-07-04 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190705_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='movies',
            field=models.ManyToManyField(related_name='favorite_movies', to='movies.Movies'),
        ),
    ]
