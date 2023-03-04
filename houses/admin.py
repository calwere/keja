from django.contrib import admin
from .models import House, Location

# admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'price')
    list_filter = ('location', 'price')
    search_fields = ('address',)

# admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'point')
    search_fields = ('name',)


# Register your models here.
