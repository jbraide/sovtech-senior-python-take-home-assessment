from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    height = models.CharField(max_length=4)
    mass = models.CharField(max_length=4)
    gender = models.CharField(max_length=8)
    homeworld = models.CharField(max_length=50)