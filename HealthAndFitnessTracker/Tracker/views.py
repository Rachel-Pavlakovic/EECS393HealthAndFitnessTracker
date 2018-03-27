from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import *
from django.shortcuts import render


def index(request):
    return HttpResponse("Please log in")


class LoginView(View):
    """ Logs in and redirects to the homepage """

    def post(self, request, *args, **kwargs):
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            if user.is_active:
                auth.login(request, user)
        return HttpResponseRedirect(reverse('Tracker:home'))

    def get(self, request, *args, **kwargs):
        # we should never get to this code path
        return HttpResponseRedirect(reverse('Tracker:home'))


def home(request):
    """ Renders home page """
    context = {
    }
    return render(request, 'home.html', context)
