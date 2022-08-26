import email
from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import SignUpForm, LoginForm
# Create your views here.


def signup_view(request):
    if not request.user.is_authenticated:
        
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'signup/signup.html', context)
    else:
        return redirect('/')
