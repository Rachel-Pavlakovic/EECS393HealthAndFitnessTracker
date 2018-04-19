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

<<<<<<< HEAD

class UserInformationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'weight', 'height', 'gender', 'units', 'notificationType', 'phoneNumber', 'email'] 
=======
>>>>>>> 914ac0928ea11b4484203107e5ecdb74e764c170
