from django.urls import reverse
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from .models import Car as Cars
from .models import Color as Colors
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

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
                self.vintage_car = vintage_car

class CarList(TemplateView):
    template_name = "car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        name = self.request.GET.get("name")
        
        if name != None:
                context["Cars"] = Cars.objects.filter(name__icontains=name)
                context["header"] = f"Searching for {name}"
        else:
                context["Cars"] = Cars.objects.all()
                context["header"] = "Trending Cars"
        return context

class CarDetail(DetailView):
        model = Cars
        template_name = "car_detail.html"
                
class CarCreate(CreateView):
        model = Cars
        fields = ['name','img','bio','vintage_car']
        template_name = "car_create.html"
        
        def get_success_url(self):
                return reverse('car_detail', kwargs={'pk': self.object.pk})
        
        
class CarUpdate(UpdateView):
        model = Cars
        fields = ['name','img','bio','vintage_car']
        template_name = "car_update.html"
        # success_url = "/cars/"
        def get_success_url(self):
                return reverse('car_detail', kwargs={'pk': self.object.pk})
        
class CarDelete(DeleteView):
    model = Cars
    template_name = "car_delete_confirmation.html"
    success_url = "/cars/"
    
class ColorCreate(CreateView):
        model = Colors
        fields = ['name','link', 'description']
        template_name = "color_create.html"
        
        def get_success_url(self):
                return reverse('color_list', kwargs={'pk': self.object.pk})

class ColorList(TemplateView):
    template_name = "color_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["colors"] = Colors.objects.all() # Here we are using the model to query the database for us.
        return context