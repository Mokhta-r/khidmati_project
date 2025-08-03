from django.shortcuts import render
from .models import Plumber
from .form import AppointmentForm

# Create your views here.

def plumbing_view(request):
    plumbers = Plumber.objects.all()
    
    selected_plumber = None
    
    
    if request.method == "POST":
        selected_id = request.POST.get("plumber")
        if selected_id:
            selected_plumber = Plumber.objects.filter(id=selected_id).first()
    
    return render(request, 'plumbing.html', {"plumbers": plumbers, "selected_plumber": selected_plumber})


def appointment_view(request):
    
    plumber_id = request.GET.get('plumber_id') or request.POST.get('selected_plumber_id')
    plumber = None
    
    if plumber_id:
        plumber = Plumber.objects.filter(id=plumber_id).first() 
        
    if request.method == 'POST':
        form = AppointmentForm(request.POST or None)
    
        if form.is_valid() :
            appointment = form.save(commit=False)
            appointment.plumber = plumber  # ✅ Assign plumber to appointment
            appointment.save()
            
            return render(request, 'appointment_success.html', {"appointment": appointment})
    else:
        form = AppointmentForm()
            
    return render(request, 'appointment.html', {"form": form, "plumber": plumber})


def home_view(request):
    """
    Render the home page.
    """
    return render(request, 'home_page.html')

