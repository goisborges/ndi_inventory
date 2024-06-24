from django.urls import path
from . import views
from django.contrib.auth import login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('staff/', views.staff, name='dashboard-staff'),
    path('', views.index, name='dashboard-index' ),
    path('products/', views.products, name='dashboard-products' ),
    path('inventory/', views.inventory, name='dashboard-inventory' ),
    path('categories/', views.categories, name='dashboard-categories'),
    path('login', auth_views.LoginView.as_view(template_name = 'user/login.html'), name = 'user-login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'user/logout.html') , name = 'user-logout')
]
