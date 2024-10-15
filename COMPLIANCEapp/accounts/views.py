from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.contrib import messages
from .forms import LoginForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if not username:
            messages.error(request, "Username cannot be empty.")
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, "Registration successful.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "Username already exists.")
            return redirect('register')

    return render(request, 'accounts/register.html')



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirect after successful login
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def landing(request):
    return render(request, 'accounts/landing.html')