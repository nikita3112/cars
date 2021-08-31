from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Car(models.Model):
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    transmission = models.SmallIntegerField(choices=[(1, "Механика"), (2, "Автомат"), (3, "Робот")])
    photo = models.ImageField(upload_to="media", null=True, blank=True)
    color = CharField(max_length=50)

    def __str__(self):
        return self.manufacturer