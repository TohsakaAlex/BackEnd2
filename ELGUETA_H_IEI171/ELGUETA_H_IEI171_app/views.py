from django.shortcuts import render

from ELGUETA_H_IEI171_app.models import Reserva
from .forms import FormReserva

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listarReservas(request):
    reserva = Reserva.objects.all()
    data = {'reserv' : reserva}
    return render(request, 'reservas.html', data)

def agregaReservas(request):
    form = FormReserva()

    if (request.method == 'POST'):
        form = FormReserva(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
    
    data = {'form': form}
    return render(request, 'agregar.html', data)

def eliminarReservas(request):
    form = FormReserva()

    if (request.method == 'DELETE'):
        form = FormReserva(request.DELETE)
        if (form.is_valid()):
            form.delete()
        return index(request)
    
    data = {'form': form}
    return render(request, 'eliminar.html', data)

def actualizarReserva(request):
    form = FormReserva()

    if (request.method == 'POST'):
        form = FormReserva(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)