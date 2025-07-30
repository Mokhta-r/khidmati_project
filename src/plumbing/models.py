from urllib import request
from django.db import models
from django import forms
# Create your models here.
class Plumber(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()
    rating = models.FloatField()
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    plumber = models.ForeignKey(Plumber, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=20)
    appointment_date = models.DateTimeField(default=None )
    notes = models.TextField(blank=True, null=True)

    


    