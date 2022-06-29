# from django.shortcuts import render
# line above, auto populated - needed ??
from django.views.generic import TemplateView


class HomePageView(TemplateView):
  template_name = 'pages/home.html'

class HomeInPageView(TemplateView):
  template_name = 'pages/home_in.html'

class AboutPageView(TemplateView):
  template_name = 'pages/about.html'

# Create your views here.
