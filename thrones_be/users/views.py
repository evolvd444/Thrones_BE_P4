from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password is incorrect")

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, "User is logged out.")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was successfully created!")

            login(request, user)
            return redirect('profiles')

        else:
            messages.success(request, 'An error has occured during registration')

    context = {'page':page, 'form': form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request):
    return render(request, 'users/user-profile.html')
