# Generated by Django 2.2.3 on 2019-07-04 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190705_0446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='movies',
        ),
    ]
