from django.shortcuts import render
from django.contrib.auth import login, logout, decorators
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import json
from images.models import Image
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@decorators.login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        email = request.POST.get('email', user.email)

        user.email = email
        user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')
    
    liked_images = Image.objects.filter(liked_by=request.user)

    return render(request, 'profile.html', {
        'user': request.user,
        'liked_images': liked_images
    })


@decorators.login_required
def delete_user_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('register')
    return render(request, 'delete.html')

@decorators.login_required
def logout_view(request):
    logout(request)
    return redirect('login')