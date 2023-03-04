from django.contrib.gis.geos import Point
from django.core.serializers import serialize
from rest_framework import serializers
from rest_framework_gis.fields import GeometrySerializerMethodField

from .models import House
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class HouseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = House
        fields = "__all__"
        geo_field = "location"
