from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.staff, name='dashboard-staff'),
    path('', views.index, name='dashboard-index' ),
    path('products/', views.products, name='dashboard-products' ),
    path('inventory/', views.inventory, name='dashboard-inventory' ),
    path('categories/', views.categories, name='dashboard-categories')
]
