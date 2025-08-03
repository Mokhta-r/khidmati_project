from django.shortcuts import render
from .models import Electrition
from .forms import AppointmentForm

def electrition_view(request):
    electrition_list = Electrition.objects.all()
    selected_electrition = None

    if request.method == "POST":
        selected_id = request.POST.get("electrition")
        if selected_id:
            selected_electrition = Electrition.objects.filter(id=selected_id).first()

    return render(request, 'electritions.html', {
        "electrition_list": electrition_list,
        "selected_electrition": selected_electrition
    })

def appointment_view(request):
    electrition_id = request.GET.get('electrition_id') or request.POST.get('selected_electrition_id')
    electrition = None

    if electrition_id:
        electrition = Electrition.objects.filter(id=electrition_id).first()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.electrition = electrition
            appointment.save()
            return render(request, 'appointment_success.html', {"appointment": appointment})
    else:
        form = AppointmentForm()

    return render(request, 'elec_appointment.html', {"form": form, "electrition": electrition})