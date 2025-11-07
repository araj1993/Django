from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomLoginForm


def register_view(request):
    """
    Handle user registration
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """
    Handle user login
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Try to authenticate with username first, then email
            user = authenticate(request, username=username, password=password)
            
            # If authentication failed with username, try with email
            if user is None:
                try:
                    user_obj = User.objects.get(email=username)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                
                # Redirect to next parameter if it exists, otherwise to dashboard
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username/email or password.')
    else:
        form = CustomLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    Handle user logout
    """
    if request.user.is_authenticated:
        username = request.user.first_name or request.user.username
        logout(request)
        messages.success(request, f'You have been logged out successfully, {username}!')
    return redirect('home')


@login_required
def dashboard_view(request):
    """
    User dashboard - protected route
    """
    context = {
        'user': request.user,
        'total_orders': request.user.order_set.count() if hasattr(request.user, 'order_set') else 0,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def profile_view(request):
    """
    User profile - protected route
    """
    return render(request, 'accounts/profile.html', {'user': request.user})


def home_view(request):
    """
    Home page view
    """
    return render(request, 'store/home.html')