"""HealthAndFitnessTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Tracker.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^home', HomePageView.as_view(), name='home'),
    url(r'^foodTracker', login_required(foodTracker.as_view()), name='foodTracker'),
    url(r'^waterTracker', login_required(waterTracker.as_view()), name='waterTracker'),
    url(r'^exerciseTracker', login_required(exerciseTracker.as_view()), name='exerciseTracker'),
    url(r'^settingsAndProfile', login_required(settingsAndProfile.as_view()), name='settingsAndProfile'),
    url(r'^createUser', createUser.as_view(), name='createUser'),
    url(r'^addfood', addfood.as_view(), name='addfood'),
    url(r'^adddrink', adddrink.as_view(), name='adddrink'),
    url(r'^addexercise', addexercise.as_view(), name='addexercise'),
    url(r'^addalert', addalert.as_view(), name='addalert'),
    url(r'^admin/', admin.site.urls),
    url(r'^updateProfile', login_required(updateProfile.as_view()), name='updateProfile'),
    url(r'^alerts', login_required(alerts.as_view()), name='alerts'),
]
