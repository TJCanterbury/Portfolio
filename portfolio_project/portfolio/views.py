from django.shortcuts import render

# Create your views here.
from .models import Profile
from .models import Print
from .models import Publications

def home(request):
    profile = Profile.objects.first()  # Fetch the profile object
    return render(request, 'portfolio/home.html', {'profile': profile}) 

def prints(request):
    prints = Print.objects.all()
    return render(request, 'portfolio/prints.html', {'prints': prints})

def publications(request):
    articles = Publications.objects.all()
    return render(request, 'portfolio/publications.html', {'articles': articles})

def contact(request):
    profile = Profile.objects.first()  # Fetch the profile object
    return render(request, 'portfolio/contact.html', {'profile': profile}) 
