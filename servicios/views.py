from django.shortcuts import render, HttpResponse, redirect
from contacto.forms import FormularioContacto
from webiqlimapp.funciones.enviocorreo import enviocorreo
from webiqlimapp.models import ParamWeb

# Create your views here.
from servicios.models import Servicio

# Create your views here.

def servicios(request):
    idioma_actual='es-EU'
    try:
        param=ParamWeb.objects.get(activa=True, idioma=idioma_actual)
    except:
        param=Paramweb.objetcs.get(activa=True, idioma='es-EU')


    servicios=Servicio.objects.all()

    formulario_contacto=FormularioContacto()

    return render(request, 'servicios/servicios.html', {"servicios": servicios, 'miFormulario':formulario_contacto, 'param':param})


def verservicio(request, servicio_id):
    idioma_actual='es-EU'
    try:
        param=ParamWeb.objects.get(activa=True, idioma=idioma_actual)
    except:
        param=Paramweb.objetcs.get(activa=True, idioma='es-EU')


    servicio = Servicio.objects.get(id=servicio_id)
    
    formulario_contacto=FormularioContacto()

    return render(request, 'servicios/VerServicio.html', {"servicio": servicio, 'miFormulario':formulario_contacto, 'param':param})
