from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"You are now logged in as {username}")
                    return redirect('blog:index')
            else:
                messages.info(request, "Invalid username or password.")
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)

@login_required()
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

    


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
        else:
            form = SignupForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)