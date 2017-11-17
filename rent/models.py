from django.db import models
from django.core.validators import MinValueValidator
from decimal import *

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=20)
    age = models.SmallIntegerField(validators=[MinValueValidator(Decimal('0'))])
    rating = models.SmallIntegerField(default=0)
    ACQUISITION_METHODS = (
        ('1', 'Delivery'),
        ('2', 'Pickup'),
        ('3', 'Delivery & Pickup'),
        ('4', 'Other Delivery'),
    )
    method = models.CharField(max_length=1, choices=ACQUISITION_METHODS, default='C')
    price = models.DecimalField(default=1.00, max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    lat = models.DecimalField(default=0.0000000, max_digits=10, decimal_places=8)
    lng = models.DecimalField(default=0.00000000, max_digits=11, decimal_places=8)
    posted = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
