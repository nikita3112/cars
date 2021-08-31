from django.urls import path, include
from CarsApp.views import CarsView

app_name = "CarsApp"
urlpatterns = [
    path('', CarsView, name="cars_list")
]
