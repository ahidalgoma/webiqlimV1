from django.shortcuts import render, HttpResponse, redirect
from contacto.forms import FormularioContacto
from webiqlimapp.funciones.enviocorreo import enviocorreo
from webiqlimapp.models import ParamWeb

# Create your views here.

def contacto(request):
    idioma_actual='es-EU'
    try:
        param=ParamWeb.objects.get(activa=True, idioma=idioma_actual)
    except:
        param=Paramweb.objetcs.get(activa=True, idioma='es-EU')

    if request.method=="POST":
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")            
            if enviocorreo(nombre, email, contenido):
                return redirect ('/contacto/?valido')
    else:
        formulario_contacto=FormularioContacto()
    
    privacidad=False
    
    return render(request, 'contacto/contacto.html', {'miFormulario':formulario_contacto, 'privacidad':privacidad, 'param':param})

