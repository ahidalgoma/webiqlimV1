from django.shortcuts import render, HttpResponse, redirect
from contacto.forms import FormularioContacto
from webiqlimapp.funciones.enviocorreo import enviocorreo

# Create your views here.
from servicios.models import Servicio

# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()

    formulario_contacto=FormularioContacto()

    return render(request, 'servicios/servicios.html', {"servicios": servicios, 'miFormulario':formulario_contacto})

