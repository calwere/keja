from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class House(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    price = models.IntegerField()

class Location(models.Model):
    name = models.CharField(max_length=255)
    point = models.PointField()


    def __str__(self):
        return self.name
