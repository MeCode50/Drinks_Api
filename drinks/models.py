from django.db import models 

# create a class and inherit from Model
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

