from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
from .models import Blog

admin.site.register(Blog)

# Register your models here.
from .models import Print
# Register the Print model with the admin interface
admin.site.register(Print)

from .models import Publications

admin.site.register(Publications)


from .models import Images
admin.site.register(Images)
