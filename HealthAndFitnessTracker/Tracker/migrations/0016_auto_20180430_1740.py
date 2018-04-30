# Generated by Django 2.0.3 on 2018-04-30 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0015_auto_20180429_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='id',
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='notificationType',
            field=models.CharField(choices=[('EMAIL', 'email'), ('PHONE', 'phone'), ('WEB', 'web')], max_length=5),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='units',
            field=models.CharField(choices=[('IMPERIAL', 'Imperial'), ('METRIC', 'Metric')], max_length=8),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
