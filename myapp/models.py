
from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length= 255)
    email = models.EmailField(max_length=254, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=255)
    #def __str__(self):
     #  return self.name
