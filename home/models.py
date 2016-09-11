from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand,related_name='car_barnd')
    color = models.CharField(max_length=100)
    milage = models.FloatField()
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name