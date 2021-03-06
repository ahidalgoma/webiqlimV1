from django.shortcuts import render, HttpResponse, redirect
from webiqlimapp.forms import FormularioContacto
from django.core.mail import EmailMessage
import os
from dotenv import load_dotenv

# Create your views here.
from servicios.models import Servicio

# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            load_dotenv()
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            email=EmailMessage("Mensaje desde la web de Iqlim",
            "el usuario con nombre {} con el mail {} escribe: \n\n {}".format(nombre, email,contenido),
            os.getenv('CO_MAIL'),[os.getenv('CO_MAIL')],reply_to=[email])

            try:
                email.send()
                return redirect ('/servicios/?valido')
            except:
                return redirect ('/servicios/?NOvalido')
    else:
        formulario_contacto=FormularioContacto()

    return render(request, 'servicios/servicios.html', {"servicios": servicios, 'miFormulario':formulario_contacto})