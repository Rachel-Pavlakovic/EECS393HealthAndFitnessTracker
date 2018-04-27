from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.conf import settings
from django.utils import timezone


class DrinkInformation(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    calPerFlOz = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

      
class FoodInformation(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    density = models.FloatField(default=0.0)
    caloricDensity = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class ExerciseInformation(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    calPerHour = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class UserInformation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gender = models.CharField(max_length=25)

    UNITCHOICE = (
        (0, 'Imperial'),
        (1, 'Metric'),
    )
    NOTIFCHOICE = (
        (0, 'email'),
        (1, 'phone'),
        (2, 'web'),
    )

    units = models.CharField(max_length=1, choices = UNITCHOICE)
    notificationType = models.CharField(max_length=1, choices = NOTIFCHOICE)
    phoneNumber = models.CharField(max_length=10)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class FoodLog(models.Model):
    info = models.ForeignKey(
        'FoodInformation',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(default=0)
    #usage
    date = models.DateTimeField(default=datetime.now())
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.info.name

class DrinkLog(models.Model):
    info = models.ForeignKey(
        'DrinkInformation',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.info.name

class ExerciseLog(models.Model):
    info = models.ForeignKey(
        'ExerciseInformation',
        on_delete=models.CASCADE,
    )
    duration = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.info.name