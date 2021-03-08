from django.shortcuts import render, HttpResponse, redirect
from contacto.forms import FormularioContacto
from webiqlimapp.funciones.enviocorreo import enviocorreo
from .models import Post
from datetime import date

# Create your views here.

pagina_activa=1

def cargar_tabla(posts, pagina_inicio):
    if pagina_inicio != 1:
        fila_inicio=((pagina_inicio-1)*3)+1
    else:
        fila_inicio=1
    posts = Post.objects.all()[fila_inicio-1:fila_inicio+2]
    return posts


def blog(request):
    posts=[]
# Se calcula el numero de paginas que debe aparecer en el pie
    paginas_totales=round(Post.objects.all().count()/3)
    if Post.objects.all().count()/3 > paginas_totales:
        paginas_totales+=1
# --------------
    posts=cargar_tabla(posts, pagina_activa)    


    formulario_contacto=FormularioContacto()

    return render(request, 'blog/blog.html', {"posts": posts, 'miFormulario':formulario_contacto, 
    "paginas_totales":paginas_totales, "pagina_activa":pagina_activa})


def verblog(request, post_id):
    post = Post.objects.get(id=post_id)
    
    formulario_contacto=FormularioContacto()

    return render(request, 'blog/VerBlog.html', {"post": post, 'miFormulario':formulario_contacto})


def paginablog(request, pagina):
    numero_pagina=pagina
    posts=[]
# Se calcula el numero de paginas que debe aparecer en el pie
    paginas_totales=round(Post.objects.all().count()/3)
    if Post.objects.all().count()/3 > paginas_totales:
        paginas_totales+=1

    posts=cargar_tabla(posts, numero_pagina)    


    formulario_contacto=FormularioContacto()

    return render(request, 'blog/blog.html', {"posts": posts, 'miFormulario':formulario_contacto, 
    "paginas_totales":paginas_totales, "pagina_activa":numero_pagina})
