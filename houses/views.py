from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import House, Location
from .serializers import HouseSerializer

class HouseList(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class HouseDetail(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    
