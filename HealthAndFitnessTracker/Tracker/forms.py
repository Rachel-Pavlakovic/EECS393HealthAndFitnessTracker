from django.forms import *
from .models import *
from django.contrib.auth.models import User

class FoodForm(ModelForm):
    class Meta:
        model = FoodInformation
        fields = ['name', 'density', 'caloricDensity']

class DrinkForm(ModelForm):
    class Meta:
        model = DrinkInformation
        fields = ['name', 'calPerFlOz']

class ExerciseForm(ModelForm):
    """
    For storing exercise information
    """
    class Meta:
        model = ExerciseInformation
        fields = ['name', 'calPerHour']

class UserInformationForm(ModelForm):
    class Meta:
        model = User
       # fields = ['username', 'password', 'weight', 'height', 'gender', 'units', 'notificationType', 'phoneNumber', 'email']
        fields = ['username', 'password', 'email']

