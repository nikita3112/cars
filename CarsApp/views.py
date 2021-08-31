from typing import List
from django.db import models
from django.shortcuts import render
from CarsApp.models import Car
from django.shortcuts import render
from django.db.models import Q


# Create your views here.
def CarsView(request):
    if request.GET:
        print(request.GET)
        manufacturer = request.GET.get('manufacturer', '')
        if not manufacturer:
            manufacturer = ''
        year_from = request.GET.get('year_from', '')
        if not year_from:
            year_from = 0
        year_to = request.GET.get('year_to', '')
        if not year_to:
            year_to = 10000
        transmission_mkpp = request.GET.get('transmission_mkpp', '')
        if transmission_mkpp == "on":
            transmission_mkpp = 1
        else:
            transmission_mkpp = 0
        transmission_akpp = request.GET.get('transmission_akpp', '')
        if transmission_akpp == "on":
            transmission_akpp = 2
        else:
            transmission_akpp = 0
        transmission_robot = request.GET.get('transmission_robot', '')
        if transmission_robot == "on":
            transmission_robot = 3
        else:
            transmission_robot = 0
        
        if transmission_mkpp != 0 or transmission_akpp != 0 or transmission_robot != 0:
            res = Q(transmission__in=[transmission_mkpp, transmission_akpp, transmission_robot])
        else:
            res = Q(transmission__in=[1,2,3])
        data = Car.objects.filter(Q(manufacturer__contains=manufacturer) & Q(year__gte=year_from) & Q(year__lte=year_to) & res)
        print(manufacturer, year_from, year_to)
    else:    
        data = Car.objects.all()
    return render(request, 'index.html', {'cars': data})