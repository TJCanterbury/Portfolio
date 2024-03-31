# portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Define additional URL patterns here
    path('prints/',views.prints, name='prints'),
    path('publications/',views.publications, name='publications'),
    path('contact/',views.contact, name='contact')
]