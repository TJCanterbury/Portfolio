from django.contrib import admin

from .models import Profile

admin.site.register(Profile)

# Register your models here.
from .models import Print

# Register the Print model with the admin interface
admin.site.register(Print)

from .models import Publications

admin.site.register(Publications)