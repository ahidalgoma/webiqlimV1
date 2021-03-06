from django.shortcuts import render, HttpResponse, redirect
from webiqlimapp.forms import FormularioContacto
from django.core.mail import EmailMessage
from .models import Post
import os
from dotenv import load_dotenv
from datetime import date

# Create your views here.


def blog(request):
    if (Post.objects.all().count()>100):
        posts = Post.objects.filter(created__year=date.today().year).order_by("-created")
    else:
        posts = Post.objects.all().order_by("-created")
    

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
                return redirect ('/blog/?valido')
            except:
                return redirect ('/blog/?NOvalido')
    else:
        formulario_contacto=FormularioContacto()

    return render(request, 'blog/blog.html', {"posts": posts, 'miFormulario':formulario_contacto})
