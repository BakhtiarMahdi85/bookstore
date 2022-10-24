from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomepageViews(TemplateView):
    template_name = 'home.html'



