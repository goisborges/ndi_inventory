from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to NDI inventory control</h1>')

def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def products(request):
    return render(request, 'dashboard/products.html')

def inventory(request):
    return render(request, 'dashboard/inventory.html')

def categories(request):
    return render(request, 'dashboard/categories.html')