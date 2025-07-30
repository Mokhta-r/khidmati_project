"""
URL configuration for khidmati project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from plumbing.views import plumbing_view, home_view, appointment_view

from services.views import service_list

urlpatterns = [
    path('plumbing', plumbing_view, name='plumbing_home'),
    
    path('appointment', appointment_view, name='appointment'),
    
    path('appointment_success', appointment_view, name='appointment_success'),
    
    path('services', service_list, name='services'),
    
    path('', home_view, name='home'),
    
    path('admin/', admin.site.urls),
]
