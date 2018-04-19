from django.views.generic.base import TemplateView
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
import datetime


class HomePageView(TemplateView):

    template_name = "home.html"

class foodTracker(TemplateView):

    template_name = "foodTracker.html"

class waterTracker(TemplateView):

    template_name = "waterTracker.html"

class exerciseTracker(TemplateView):

    template_name = "exerciseTracker.html"

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
