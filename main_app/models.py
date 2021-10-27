from django.db import models

# Create your models here.

class Car(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    vintage_car = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        
class Color(models.Model):

    description = models.CharField(max_length=100, default="Describe Color")
    link = models.CharField(max_length=150)
    name = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="colors", default=Car.name)

    def __str__(self):
        return self.description