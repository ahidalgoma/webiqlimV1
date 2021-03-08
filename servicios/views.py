from django.shortcuts import render, HttpResponse, redirect
from webiqlimapp.forms import FormularioContacto
from webiqlimapp.funciones.enviocorreo import enviocorreo

# Create your views here.
from servicios.models import Servicio

# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")            
            if enviocorreo(nombre, email, contenido):
                return redirect ('/servicios/?valido')
            else:
                return redirect ('/servicios/?NOenvio')
        else:
           return redirect ('/servicios/?NOcorrectoscampos')
    else:
        formulario_contacto=FormularioContacto()

    return render(request, 'servicios/servicios.html', {"servicios": servicios, 'miFormulario':formulario_contacto})