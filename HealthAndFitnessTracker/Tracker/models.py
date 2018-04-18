from django.db import models
from django.forms import ModelForm
import datetime
from enum import Enum

class unit(Enum):
    Imperial = 0
    Metric = 1

class notif(Enum):
    email = 0
    phone = 1
    web = 2


class DrinkInformation(models.Model):
    name = models.CharField(max_length=128)
    calPerFlOz = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

      
class FoodInformation(models.Model):
    name = models.CharField(max_length=128)
    denisty = models.FloatField()
    caloricDensity = models.FloatField()

    def __str__(self):
        return self.name


class ExerciseInformation(models.Model):
    name = models.CharField(max_length=128)
    calPerHour = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=128)
    passord = models.CharField(max_length=128)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gender = models.CharField(max_length=25)
    units = unit
    notificationType = notif
    phoneNumber = models.CharField(max_length=10)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class FoodLog(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField(default=0)
    date = models.DateField()
    time = models.TimeField()
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class DrinkLog(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField(default=0)
    date = models.DateField()
    time = models.TimeField()
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class ExerciseLog(models.Model):
    name = models.CharField(max_length=128)
    duration = models.IntegerField(default=0)
    date = models.DateField()
    time = models.TimeField()
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(User)

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


class UserInformationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'weight', 'height', 'gender', 'units', 'notificationType', 'phoneNumber', 'email'] 
