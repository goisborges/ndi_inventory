
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            # Redirect to dashboard after user creation
            return redirect('dashboard-index')
    else:
        form = CreateUserForm()
    context = {
        'form': form

    }
    return render(request, 'user/register.html', context)

def  login(request):
    return render(request,'user/login.html'),{}


