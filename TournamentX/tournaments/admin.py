from django.contrib import admin
from .models import User, Tournament, Team


# Register your models here.

admin.site.register([User, Tournament, Team])
