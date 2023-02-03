from django.db import models

# Create your models here.

class House(models.Model):
    '''houses model'''
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(verbose_name="Price per night")
    description = models.TextField()
    address = models.CharField(max_length=140)

    pets_ok = models.BooleanField(verbose_name = "pets allowd?", 
                                  default=True, 
                                  help_text="Does this house allow pets???", 
                                  )

    def __str__(self):
        return self.name
    

    