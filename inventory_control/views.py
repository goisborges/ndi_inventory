from django.shortcuts import render

# Create your views here.
# request -> response
# request handler
# action

from django.http import HttpResponse

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Marcos B'})