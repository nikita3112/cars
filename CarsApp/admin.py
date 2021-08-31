from django.contrib import admin
from CarsApp.models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass