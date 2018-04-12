from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('soundbuddy/', include('soundbuddy.urls')),
    path('admin/', admin.site.urls),
]
