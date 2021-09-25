from django.shortcuts import render

# Create your views here.

def profiles(request):
    return render(request, 'users/profiles.html')

def profile(request):
    return render(request, 'users/profile.html')