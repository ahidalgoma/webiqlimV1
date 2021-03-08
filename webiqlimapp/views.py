from django.shortcuts import render, HttpResponse, redirect
from contacto.forms import FormularioContacto
from webiqlimapp.funciones.enviocorreo import enviocorreo



# Create your views here.

def home(request):

    formulario_contacto=FormularioContacto()

    return render(request, 'webiqlimapp/home.html', {'miFormulario':formulario_contacto})

