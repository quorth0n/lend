from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    rating = models.SmallIntegerField(default=-1)
    PICKUP_METHODS = (
        ('C', 'Car'),
    )
    method = models.CharField(max_length=1, choices=PICKUP_METHODS, default='C')
    price = models.DecimalField(default=-1.00, max_digits=6, decimal_places=2)
    lat = models.DecimalField(default=0.0000000, max_digits=10, decimal_places=8)
    lng = models.DecimalField(default=0.00000000, max_digits=11, decimal_places=8)
    
