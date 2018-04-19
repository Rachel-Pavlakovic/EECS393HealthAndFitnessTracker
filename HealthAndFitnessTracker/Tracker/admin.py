from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(FoodLog)
admin.site.register(DrinkLog)
admin.site.register(ExerciseLog)
admin.site.register(User)