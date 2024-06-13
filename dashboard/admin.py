from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models

# Register your models here.

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'location', 'category')
    list_filter = ('name','category')

admin.site.register(Product, ProductAdmin) 
admin.site.register(Category)
admin.site.register(Location)

#change the admin site header
admin.site.site_header = 'NDI Inventory Admin Site'


