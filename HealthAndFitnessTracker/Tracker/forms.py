<<<<<<< HEAD
from django.forms import ModelForm
from .models import FoodInformation
from .models import DrinkInformation
from .models import ExerciseInformation
=======
from django.forms import *
from .models import *
from django.contrib.auth.models import User
>>>>>>> 914ac0928ea11b4484203107e5ecdb74e764c170

class FoodForm(ModelForm):
    class Meta:
        model = FoodInformation
        fields = ['name', 'density', 'caloricDensity']

<<<<<<< HEAD
# Creating a form to add food info
foodForm = FoodForm()

# Creating a form to change an existing article.
food = FoodInformation.objects.get(pk=1)
foodForm = FoodForm(instance=food)


=======
>>>>>>> 914ac0928ea11b4484203107e5ecdb74e764c170
class DrinkForm(ModelForm):
    class Meta:
        model = DrinkInformation
        fields = ['name', 'calPerFlOz']

<<<<<<< HEAD
# Creating a form to add drink information
drinkForm = DrinkForm()

# Creating a form to change an existing article.
drink = DrinkInformation.objects.get(pk=1)
drinkForm = DrinkForm(instance=food)

=======
>>>>>>> 914ac0928ea11b4484203107e5ecdb74e764c170
class ExerciseForm(ModelForm):
    class Meta:
        model = ExerciseInformation
        fields = ['name', 'calPerHour']

<<<<<<< HEAD
# Creating a form to add drink information
exerciseForm = ExerciseForm()

# Creating a form to change an existing article.
exercise = ExerciseInformation.objects.get(pk=1)
exerciseForm = ExerciseForm(instance=food)
=======
class UserInformationForm(ModelForm):
    class Meta:
        model = User
       # fields = ['username', 'password', 'weight', 'height', 'gender', 'units', 'notificationType', 'phoneNumber', 'email']
        fields = ['username', 'password', 'email']
>>>>>>> 914ac0928ea11b4484203107e5ecdb74e764c170
