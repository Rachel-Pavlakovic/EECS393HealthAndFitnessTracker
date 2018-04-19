from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DrinkInformation)
admin.site.register(FoodInformation)
admin.site.register(ExerciseInformation)
admin.site.register(User)
admin.site.register(FoodLog)
admin.site.register(DrinkLog)
admin.site.register(ExerciseLog)