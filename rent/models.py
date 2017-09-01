from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=20)
    age = models.SmallIntegerField()
