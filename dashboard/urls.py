from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.staff, name='staff'),
    path('', views.index, name='index' )
]
