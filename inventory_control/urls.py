from django.urls import path
from . import views

app_name = "inventory_control"
urlpatterns = [
    path('hello/', views.say_hello)
]