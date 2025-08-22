from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from tournaments import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tournaments.urls')), 
]
