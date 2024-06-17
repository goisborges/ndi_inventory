from operator import is_
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            # Redirect to dashboard after user creation
            return redirect('dashboard-index')
    else:
        form = UserCreationForm()
    context = {
        'form': form

    }
    return render(request, 'user/register.html', context)

def  login(request):
    return render(request,'user/login.html'),{}


