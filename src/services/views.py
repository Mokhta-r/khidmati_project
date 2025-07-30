from django.shortcuts import render
from .models import Service

# Create your views here.

def service_list(request, *args, **kwargs):
    """Render the list of services.
    """
    
    services = Service.objects.all()
    
    
    return render(request, 'services.html', {'services': services})