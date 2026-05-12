from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models, authenticate, login, logout
from .forms import RegisterForm
from .models import UserToken
from django.core.mail import send_mail
from django.contrib.auth.models import User
import secrets

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

def send_magic_link_mail(user, email, token):
    
    link = f"http://127.0.0.1:8000/accounts/magic-verify/?token={token}"

    send_mail(
        subject='Portfolio Login Link',
        message=f"Hello {user.first_name},\n\nClick here to login:\n{link}",
        from_email='email.app@me.com',
        recipient_list=[email]
    )

def login_magic_link(request):

    if request.method == "POST":
        
        email = request.POST['email']

        if not email:
            
            return redirect('accounts:magic_login', {
                'message':'Email not found!'
            })

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return redirect('accounts:login')

        token = secrets.token_urlsafe(32)

        UserToken.objects.create(user=user, token=token)

        send_magic_link_mail(user, email, token)

        return render(request, 'accounts/magic_login.html', {
            'message': 'Magic link sent to your email'
        })
        
    return render(request, 'accounts/magic_login.html')

def login_magic_link_verify(request):

    token = request.GET.get('token')

    try:
        magic = UserToken.objects.get(token=token)
    except UserToken.DoesNotExist:
        return redirect('accounts:login')

    login(request, magic.user)

    magic.delete()

    return redirect('accounts:user')
