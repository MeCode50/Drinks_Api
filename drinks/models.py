from django.db import models 

# create a class and inherit from Model
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
# display the name of the drink and description
    def __str__(self):
        return self.name + ': '  + self.description 