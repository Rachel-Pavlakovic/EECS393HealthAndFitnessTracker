from django.forms import ModelForm
from models import FoodInformation
from models import DrinkInformation
from models import ExerciseInformation

class FoodForm(ModelForm):
    class Meta:
        model = FoodInformation
        fields = ['name', 'density', 'caloricDensity']

# Creating a form to add food info
foodForm = FoodForm()

# Creating a form to change an existing article.
food = FoodInformation.objects.get(pk=1)
foodForm = FoodForm(instance=food)


class DrinkForm(ModelForm):
    class Meta:
        model = DrinkInformation
        fields = ['name', 'calPerFlOz']

# Creating a form to add drink information
drinkForm = DrinkForm()

# Creating a form to change an existing article.
drink = DrinkInformation.objects.get(pk=1)
drinkForm = DrinkForm(instance=food)

class ExerciseForm(ModelForm):
    """
    For storing exercise information
    """
    class Meta:
        model = ExerciseInformation
        fields = ['name', 'calPerHour']

# Creating a form to add drink information
exerciseForm = ExerciseForm()

# Creating a form to change an existing article.
exercise = ExerciseInformation.objects.get(pk=1)
exerciseForm = ExerciseForm(instance=food)