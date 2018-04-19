from django.views.generic.base import TemplateView
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import *

class HomePageView(TemplateView):
    template_name = "home.html"

class foodTracker(ListView):
    template_name = "foodTracker.html"

    def get_queryset(self):
        return FoodLog.objects.all()


class waterTracker(TemplateView):

    template_name = "waterTracker.html"

class exerciseTracker(TemplateView):

    template_name = "exerciseTracker.html"

class settingsAndProfile(TemplateView):

    template_name = "settingsAndProfile.html"

class createUser(FormView):

    template_name = "createUser.html"
    form_class = UserInformationForm
    success_url = '/home'

    def post(self, request):
        if request.method == "POST":
            form = UserInformationForm(request.POST)
            if form.is_valid():
                new_user = User.objects.create_user(**form.cleaned_data)
                # redirect, or however you want to get to the main view
                return HttpResponseRedirect('/home/')
        else:
            form = UserInformationForm()

        return render(request, 'createUser.html', {'form': form})


