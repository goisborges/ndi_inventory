# from ast import Delete
# from tkinter import CASCADE
# from django.db import models

# # Create your models here.
# from os import name
# from unicodedata import category
# from django.contrib.auth.models  import User
# from dashboard.models import Product



# # Create your models here.

# class PMKit(models.Model):
#     date = models.DateField('Date')
#     user = models.ForeignKey('UserProfile', on_delete = models.CASCADE, null = True)
#     product = models.ForeignKey(Product, on_delete = models.SET_NULL, related_name='products', null=True)
#     recipient_doctor = models.CharField('Recipient Doctor', max_length=200)
#     laser_SN  = models.CharField('Laser SN', max_length=8,)



#     def __str__(self):
#         return f'{self.date} / {self.date}'