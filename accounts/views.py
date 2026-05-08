from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models, authenticate, login, logout
from .forms import RegisterForm

def register_user_view(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('accounts:login')
    
    context = { 'form': form }
        
    return render(request, 'accounts/register.html', context)

def login_user_view(request):
    
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'portfolio/index.html')
        else:
            return render(request, 'accounts/login.html', {
                'message':'Invalid Login Information!'
            })
        
    return render(request, 'accounts/login.html')

@login_required
def logout_user_view(request):
    
    logout(request)
    return redirect('portfolio:index')

@login_required
def user_view(request):

    return render(request, 'accounts/user.html')
