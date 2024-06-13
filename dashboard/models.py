from os import name
from unicodedata import category
from django.db import models



# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 50, null = True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null = True)
    quantity = models.IntegerField(null = True)
    sku_number = models.CharField(max_length = 50, unique = True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null = True)
    description = models.TextField()
    photo_image = models.ImageField(upload_to='dashboard/media', null=True, blank = True)

    def __str__(self):
        return f'{self.name} / {self.quantity}'

class  Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
