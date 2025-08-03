from django.contrib import admin

# Register your models here.
from .models import Electrition, Appointment

admin.site.register(Electrition)
admin.site.register(Appointment)