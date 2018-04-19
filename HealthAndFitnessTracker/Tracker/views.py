from django.views.generic.base import TemplateView
from .forms import *
from django.views.generic.edit import FormView
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
<<<<<<< HEAD
import datetime
from django.views.generic import ListView
from .models import *
=======
from django.views.generic import ListView
import datetime

>>>>>>> 1860e1f8eb2606b6f19b0f365742ec3f7c03e0dc

class HomePageView(TemplateView):

    template_name = "home.html"

class foodTracker(ListView):
    template_name = "foodTracker.html"

    def get_queryset(self):
        return FoodLog.objects.all()


class waterTracker(ListView):
    template_name = "waterTracker.html"

    def get_queryset(self):
        return DrinkLog.objects.all()

class exerciseTracker(ListView):
    template_name = "exerciseTracker.html"

    def get_queryset(self):
        return ExerciseLog.objects.all()

class settingsAndProfile(TemplateView):

    template_name = "settingsAndProfile.html"

class createUser(FormView):

    template_name = "createUser.html"
    form_class = UserInformationForm

    def post(self, request):
        if request.method == "POST":
            form = UserInformationForm(request.POST)
            if form.is_valid():
                User.objects.create_user(**form.cleaned_data)
                # redirect, or however you want to get to the main view
                return HttpResponseRedirect('/home/')
        else:
            form = UserInformationForm()

        return render(request, 'createUser.html', {'form': form})

<<<<<<< HEAD
=======

>>>>>>> 1860e1f8eb2606b6f19b0f365742ec3f7c03e0dc
class addfood(FormView):
    template_name = "addfood.html"
    form_class = FoodForm

    def post(self, request):
        if request.method == "POST":
            form = FoodForm(request.POST)
            if form.is_valid():
                user = User.objects.get(username=request.user.username)
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                # redirect, or however you want to get to the main view
                return HttpResponseRedirect('/foodTracker/')
        else:
            form = FoodForm()

        return render(request, 'addfood.html', {'form': form})
<<<<<<< HEAD

=======
>>>>>>> 1860e1f8eb2606b6f19b0f365742ec3f7c03e0dc
