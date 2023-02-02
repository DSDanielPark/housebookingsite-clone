from django.db import models

# Create your models here.

class House(models.Model):
    '''houses model'''
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)

    pets_ok = models.BooleanField(default=True)