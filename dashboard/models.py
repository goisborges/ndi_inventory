from unicodedata import category
from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length = 50, null = True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    quantity = models.IntegerField()
    sku_number = models.CharField(max_length = 50, unique = True)
    description = models.TextField()
    photo_image = models.ImageField(upload_to='dashboard/media')


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
