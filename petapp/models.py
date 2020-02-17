from django.db import models

class PetModel(models.Model):
    name = models.CharField(max_length = 150)
    age = models.IntegerField()
    available = models.BooleanField(default = True)
    image = models.ImageField("media/")
    price = models.DecimalField(max_digits=5,decimal_places=2)
