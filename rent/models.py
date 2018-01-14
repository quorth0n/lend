from django.db import models
from django.core.validators import MinValueValidator
from decimal import *

import firebase_admin
from firebase_admin import credentials, storage

default_app = firebase_admin.initialize_app(credentials.Certificate('rent/firebase.json'), {
    'storageBucket': 'lend-inc.appspot.com'
})

bucket = storage.bucket()

# Create your models here.
class Product(models.Model):
    name = models.CharField('Product Title', max_length=50)
    owner = models.CharField(max_length=40)
    age = models.SmallIntegerField('Item Age', help_text='(In years please!)', validators=[MinValueValidator(Decimal('0'))])
    rating = models.SmallIntegerField(default=0)
    ACQUISITION_METHODS = (
        ('1', 'Delivery'),
        ('2', 'Pickup'),
        ('3', 'Delivery & Pickup'),
        ('4', 'Other Delivery Option'),
    )
    method = models.CharField('Pickup/Delivery Method', max_length=1, choices=ACQUISITION_METHODS, default='C')
    price = models.DecimalField('Price Per Hour', default=1.00, max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    lat = models.DecimalField(default=0.0000000, max_digits=10, decimal_places=8)
    lng = models.DecimalField(default=0.00000000, max_digits=11, decimal_places=8)
    posted = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def delete(self):
        print(self.pk)
        blob = bucket.blob('productImages/'+self.pk+'.jpg')
        blob.delete()


class User(models.Model):
    uname = models.SlugField(max_length=40)
    bio = models.CharField(max_length=300)
    lat = models.DecimalField(default=0.0000000, max_digits=10, decimal_places=8)
    lng = models.DecimalField(default=0.00000000, max_digits=11, decimal_places=8)
    joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.uname
