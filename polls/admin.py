from django.contrib import admin
from .models import Band, Musician

admin.site.register([Band, Musician])

