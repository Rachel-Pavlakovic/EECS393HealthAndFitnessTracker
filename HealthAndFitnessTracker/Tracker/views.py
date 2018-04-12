from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

class HomePageView(TemplateView):

    template_name = "home.html"

@login_required
class foodTracker(TemplateView):

    template_name = "foodTracker.html"

@login_required
class waterTracker(TemplateView):

    template_name = "waterTracker.html"

@login_required
class exerciseTracker(TemplateView):

    template_name = "exerciseTracker.html"

@login_required
class settingsAndProfile(TemplateView):

    template_name = "settingsAndProfile.html"