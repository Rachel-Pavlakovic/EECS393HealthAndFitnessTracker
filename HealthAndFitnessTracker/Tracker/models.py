from django.db import models
from django.forms import ModelForm
from datetime import datetime
import datetime as dt
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save


class DrinkInformation(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    calPerFlOz = models.IntegerField(default=0)

      
class FoodInformation(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    density = models.FloatField(default=0.0)
    caloricDensity = models.FloatField(default=0.0)


class ExerciseInformation(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    calPerHour = models.IntegerField(default=0)


class AlertLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)

    def upcomingonehour(self):
        return timezone.now() <= self.time and self.time <= (timezone.now() + dt.timedelta(hours=1))

    def alertlate(self):
        return self.time < timezone.now()


class UserInformation(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gender = models.CharField(max_length=25)

    UNITCHOICE = (
        ('IMPERIAL', 'Imperial'),
        ('METRIC', 'Metric'),
    )
    NOTIFCHOICE = (
        ('EMAIL', 'email'),
        ('PHONE', 'phone'),
        ('WEB', 'web'),
    )

    units = models.CharField(max_length=8, choices = UNITCHOICE)
    notificationType = models.CharField(max_length=5, choices = NOTIFCHOICE)
    phoneNumber = models.CharField(max_length=10)



class FoodLog(models.Model):
    info = models.ForeignKey(
        'FoodInformation',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(default=0)
    #usage
    date = models.DateTimeField(default=timezone.now)
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class DrinkLog(models.Model):
    info = models.ForeignKey(
        'DrinkInformation',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class ExerciseLog(models.Model):
    info = models.ForeignKey(
        'ExerciseInformation',
        on_delete=models.CASCADE,
    )
    duration = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    calories = models.IntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


#this function auto generates the calorie content of a newly created or modified drink log
@receiver(post_save, sender=DrinkLog, dispatch_uid='generate_drink_calories')
def gen_drink_calorie(sender, instance, **kwargs):
    if kwargs.get('created', False):
        temp = instance.info.calPerFlOz
        userPreference = UserInformation.objects.get(user=instance.user)
        #dividing by 29.5735 converts the calories per floz to calories per ml
        if(userPreference.units == 'METRIC'):
            total = (instance.quantity * temp) / 29.5735
        else:
            total = instance.quantity * temp
        instance.calories = int(total)
        instance.save()

#this function auto generates the calorie content of a newly created or modified drink log
@receiver(post_save, sender=FoodLog, dispatch_uid='generate_food_calories')
def gen_food_calorie(sender, instance, **kwargs):
    if kwargs.get('created', False):
        userPreference = UserInformation.objects.get(user=instance.user)
        #calorie density is cal per 100g
        #multiplying by 28.3495 converts from grams to oz (all of our math for food is in metric)
        if (userPreference.units == 'METRIC'):
            total = (instance.quantity * instance.info.caloricDensity) /100
        else:
            total = (28.3495 * instance.quantity * instance.info.caloricDensity) / 100
        instance.calories = int(total)
        instance.save()

#this function auto generates the calorie content of a newly created or modified drink log
@receiver(post_save, sender=ExerciseLog, dispatch_uid='generate_exercise_calories')
def gen_exercise_calorie(sender, instance, **kwargs):
    if kwargs.get('created', False):
        temp = instance.info.calPerHour
        total = instance.duration * temp
        instance.calories = int(total)
        instance.save()