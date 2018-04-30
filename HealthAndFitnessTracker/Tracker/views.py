from django.views.generic.base import TemplateView
from .forms import *
from django.views.generic.edit import FormView
from Tracker.models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView


class HomePageView(ListView):

    template_name = "home.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            q = AlertLog.objects.all()
            q_ids = [o.id for o in q if o.upcomingonehour()]
            query_results = AlertLog.objects.filter(id__in=q_ids, user=self.request.user)
            return query_results
        else:
            return None

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            q = AlertLog.objects.all()
            q_ids = [o.id for o in q if o.alertlate()]
            context['late_alert'] = AlertLog.objects.filter(id__in=q_ids, user=self.request.user)
            return context
        else:
            return None

class foodTracker(ListView):
    template_name = "foodTracker.html"

    def get_queryset(self):
        return FoodLog.objects.filter(user=self.request.user)


class waterTracker(ListView):
    template_name = "waterTracker.html"

    def get_queryset(self):
        return DrinkLog.objects.filter(user=self.request.user)

class exerciseTracker(ListView):
    template_name = "exerciseTracker.html"

    def get_queryset(self):
        return ExerciseLog.objects.filter(user=self.request.user)

class settingsAndProfile(ListView):

    template_name = "settingsAndProfile.html"

    def get_queryset(self):
        return UserInformation.objects.filter(user=self.request.user)

class alerts(ListView):
    template_name = "alerts.html"

    def get_queryset(self):
        return AlertLog.objects.filter(user=self.request.user)

class createUser(FormView):

    template_name = "createUser.html"
    form_class = UserForm

    def post(self, request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                User.objects.create_user(**form.cleaned_data)
                # redirect, or however you want to get to the main view
                return HttpResponseRedirect('/home/')
        else:
            form = UserForm()

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

class adddrink(FormView):
    template_name = "adddrink.html"
    form_class = DrinkForm

    def post(self, request):
        if request.method == "POST":
            form = DrinkForm(request.POST)
            if form.is_valid():
                user = User.objects.get(username=request.user.username)
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                # redirect, or however you want to get to the main view
                return HttpResponseRedirect('/waterTracker/')
        else:
            form = DrinkForm()

        return render(request, 'adddrink.html', {'form': form})

class addexercise(FormView):
    template_name = "addexercise.html"
    form_class = ExerciseForm

    def post(self, request):
        if request.method == "POST":
            form = ExerciseForm(request.POST)
            if form.is_valid():
                user = User.objects.get(username=request.user.username)
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                # redirect, or however you want to get to the main view
                return HttpResponseRedirect('/exerciseTracker/')
        else:
            form = ExerciseForm()

        return render(request, 'addexercise.html', {'form': form})

class addalert(FormView):
    template_name = "addalert.html"
    form_class = AlertForm

    def post(self, request):
        if request.method == "POST":
            form = AlertForm(request.POST)
            if form.is_valid():
                user = User.objects.get(username=request.user.username)
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                # redirect, or however you want to get to the main view
                return HttpResponseRedirect('/settingsAndProfile/')
        else:
            form = AlertForm()

        return render(request, 'alertform.html', {'form': form})

class updateProfile(FormView):
    template_name = "updateProfile.html"
    form_class = UserInformationForm

    def post(self, request):
        if request.method == 'POST':
            form = UserInformationForm(request.POST)
            if form.is_valid():
                user = User.objects.get(username=request.user.username)
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                # redirect, or however you want to get to the main view
                return HttpResponseRedirect('/settingsAndProfile/')
        else:
            form = UserInformationForm()

        return render(request, 'updateProfile.html', {'form': form})