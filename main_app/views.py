from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from .models import Car as Cars

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
        template_name = "home.html"
    
class About(TemplateView):
        template_name = "about.html"
        
class Index(TemplateView):
        template_name = "index.html"
        
class Car:
        def __init__(self, name, image, bio):
                self.name = name
                self.image = image
                self.bio = bio

class CarList(TemplateView):
    template_name = "car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Cars"] = Cars.objects.all()
        return context
