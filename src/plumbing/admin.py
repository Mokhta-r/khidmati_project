from django.contrib import admin

# Register your models here.
from .models import Plumber, Appointment

admin.site.register(Plumber)
admin.site.register(Appointment)