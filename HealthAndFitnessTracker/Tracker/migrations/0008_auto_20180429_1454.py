# Generated by Django 2.0.3 on 2018-04-29 18:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tracker', '0007_auto_20180428_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userinformation',
            name='email',
        ),
        migrations.AlterField(
            model_name='drinklog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 29, 14, 54, 44, 659349)),
        ),
        migrations.AlterField(
            model_name='exerciselog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 29, 14, 54, 44, 659851)),
        ),
        migrations.AlterField(
            model_name='foodlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 29, 14, 54, 44, 658853)),
        ),
    ]
