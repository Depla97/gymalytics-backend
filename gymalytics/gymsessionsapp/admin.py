from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register([Athlete,Exercise,Set,Session])