# Generated by Django 2.0.3 on 2018-04-27 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0002_auto_20180427_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinklog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 27, 13, 37, 21, 92410)),
        ),
        migrations.AlterField(
            model_name='exerciselog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 27, 13, 37, 21, 93415)),
        ),
        migrations.AlterField(
            model_name='foodlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 27, 13, 37, 21, 91409)),
        ),
    ]