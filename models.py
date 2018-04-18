from django.db import models
from django.forms import ModelForm

from enum import Enum
class unit(Enum):
    Imperial = 0
    Metric = 1

class notif(Enum):
    email = 0
    phone = 1
    web = 2

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

class Drink(models.Model):
    name = models.CharField(max_length=128)
    calPerFlOz = models.IntegerField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=128)
    denisty = models.FloatField()
    caloricDensity = models.FloatField()

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=128)
    calPerHour = models.IntegerField()

    def __str__(self):
        return self.name

class UserInformation(models.Model):
    username = models.CharField(max_length=128)
    weight = models.IntegerField()
    height = models.IntegerField()
    gender = models.CharField(max_length=25)
    units = unit
    notificationType = notif
    phoneNumber = models.CharField(max_length=10)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'members']


class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields = ['person', 'group', 'date_joined', 'invite_reason']


class DrinkForm(ModelForm):
    class Meta:
        model = Drink
        fields = ['name', 'calPerFlOz']


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'density', 'caloricDensity']


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'calPerHour']


class UserInformationForm(ModelForm):
    class Meta:
        model = UserInformation
        fields = ['username', 'weight', 'height', 'gender', 'units', 'notificationType', 'phoneNumber', 'email'] 