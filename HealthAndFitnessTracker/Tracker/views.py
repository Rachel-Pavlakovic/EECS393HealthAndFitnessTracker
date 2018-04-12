from django.views.generic.base import TemplateView

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