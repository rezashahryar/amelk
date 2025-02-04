from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm

# Create your views here.


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']
            user = authenticate(username=mobile, password=password)
            if user is not None:
                login(request, user)
                return redirect('pages:home')
        
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('pages:home')
    

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)
