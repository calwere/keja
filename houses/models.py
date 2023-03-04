from django.contrib.gis.db import models

class House(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.PointField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Location(models.Model):
    name = models.CharField(max_length=255)
    point = models.PointField()


    def __str__(self):
        return self.name


# Database design