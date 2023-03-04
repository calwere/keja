from django.urls import path
from .views import MapView, HouseList, HouseDetail


urlpatterns = [
    path('', MapView.as_view(), name='map'),
    path('houses', HouseList.as_view(), name='house-list'),
    path('houses/<int:pk>/', HouseDetail.as_view(), name='house-detail'),
]

# caleb.com = MAP VIEW
# caleb.com/houses = HOUSESLIST
# caleb.com/houses/1 = HOUSEDETAIL