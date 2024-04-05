# portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Define additional URL patterns here
    path('prints/',views.prints, name='prints'),
    path('publications/',views.publications, name='publications'),
    path('projects/',views.projects, name='projects'),
    path('opinions/',views.opinions, name='opinions'),
    path('heretics/',views.heretics, name='heretics'),
    path('sketches/',views.sketches, name='sketches'),
    path('contact/',views.contact, name='contact')
]