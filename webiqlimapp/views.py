from django.shortcuts import render, HttpResponse, redirect
from contacto.forms import FormularioContacto
from webiqlimapp.funciones.enviocorreo import enviocorreo
from .models import ParamWeb



# Create your views here.

def home(request):
    idioma_actual='es-EU'
    try:
        param=ParamWeb.objects.get(activa=True, idioma=idioma_actual)
    except:
        param=Paramweb.objetcs.get(activa=True, idioma='es-EU')

    formulario_contacto=FormularioContacto()

    return render(request, 'webiqlimapp/home.html', {'miFormulario':formulario_contacto, 'param':param})

