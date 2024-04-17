from django.shortcuts import render

# Create your views here.
from .models import Profile
from .models import Print
from .models import Publications
from .models import Sketches
from .models import Images
from .models import Blog


def home(request):
    profile = Profile.objects.first()  # Fetch the profile object
    return render(request, 'portfolio/home.html', {'profile': profile})

def illustrations(request):
    illus = Images.objects.all().filter(category="illus")
    return render(request, 'portfolio/illustrations.html', {'illus': illus})

def publications(request):
    articles = Publications.objects.all()
    return render(request, 'portfolio/publications.html', {'articles': articles})

def contact(request):
    profile = Profile.objects.first()  # Fetch the profile object
    return render(request, 'portfolio/contact.html', {'profile': profile})

def projects(request):
    return render(request, 'portfolio/projects.html')

def opinions(request):
    blog = Blog.objects.all()  # Fetch the profile object
    return render(request, 'portfolio/opinions.html', {'blog': blog})

def heretics(request):
    return render(request, 'portfolio/heretics.html')

def sketches(request):
    sketches = Images.objects.all().filter(category="sketch")
    return render(request, 'portfolio/sketches.html', {'sketches': sketches})
