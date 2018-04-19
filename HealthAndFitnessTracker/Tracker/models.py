from django.db import models
from django.forms import ModelForm
import datetime

class DrinkInformation(models.Model):
    name = models.CharField(max_length=128)
    calPerFlOz = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

      
class FoodInformation(models.Model):
    name = models.CharField(max_length=128)
    density = models.FloatField(default=0.0)
    caloricDensity = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class ExerciseInformation(models.Model):
    name = models.CharField(max_length=128)
    calPerHour = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gender = models.CharField(max_length=25)

    UNITCHOICE = (
        ('IMPERIAL', 'imperial'),
        ('METRIC', 'metric'),
    )
    NOTIFCHOICE = (
        ('EMAIL', 'email'),
        ('PHONE', 'phone'),
        ('WEB', 'web'),
    )

    units = models.CharField(max_length=10, choices = UNITCHOICE, default = 'IMPERIAL')
    notificationType = models.CharField(max_length=10, choices = NOTIFCHOICE, default = 'EMAIL')
    phoneNumber = models.CharField(max_length=10)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class FoodLog(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField(default=0)
    date = models.DateField()
    time = models.TimeField()
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class DrinkLog(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField(default=0)
    date = models.DateField()
    time = models.TimeField()
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class ExerciseLog(models.Model):
    name = models.CharField(max_length=128)
    duration = models.IntegerField(default=0)
    date = models.DateField()
    time = models.TimeField()
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name



class DrinkForm(ModelForm):
    class Meta:
        model = DrinkInformation
        fields = ['name', 'calPerFlOz']


class FoodForm(ModelForm):
    class Meta:
        model = FoodInformation
        fields = ['name', 'density', 'caloricDensity']


class ExerciseForm(ModelForm):
    class Meta:
        model = ExerciseInformation
        fields = ['name', 'calPerHour']

