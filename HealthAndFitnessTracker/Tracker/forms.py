from django.forms import *
from .models import *
from django.contrib.auth.models import User

class FoodForm(ModelForm):
    class Meta:
        model = FoodLog
        fields = ['info','quantity', 'date']

class DrinkForm(ModelForm):
    class Meta:
        model = DrinkLog
        fields = ['info','quantity', 'date']

class ExerciseForm(ModelForm):
    class Meta:
        model = ExerciseLog
        fields = ['info','duration', 'date']

class UserInformationForm(ModelForm):
    class Meta:
        model = UserInformation
       # fields = ['username', 'password', 'weight', 'height', 'gender', 'units', 'notificationType', 'phoneNumber', 'email']
        fields = ['email']
