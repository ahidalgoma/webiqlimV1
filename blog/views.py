from django.shortcuts import render, HttpResponse, redirect
from contacto.forms import FormularioContacto
from webiqlimapp.funciones.enviocorreo import enviocorreo
from django.db.models import Q
from .models import Post
from datetime import date
import math

# Create your views here.

pagina_activa=1

def cargar_tabla(pagina_inicio):

    if pagina_inicio != 1:
        fila_inicio=((pagina_inicio-1)*3)+1
    else:
        fila_inicio=1
    posts = Post.objects.filter(publicar=True)[fila_inicio-1:fila_inicio+2]
    # Se calcula el numero de paginas que debe aparecer en el pie
    Total_Posts = Post.objects.filter(publicar=True).count()
    paginas_totales=math.ceil(Total_Posts/3)
    
    return {'posts':posts, 'paginas_totales':paginas_totales}


def blog(request):
    paginas_totales=1
    posts=[]
# --------------
    posts_dic=cargar_tabla(pagina_activa)
    posts=posts_dic.get('posts')
    paginas_totales=posts_dic.get('paginas_totales')


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
    paginas_totales=1
    posts_dic=cargar_tabla(pagina)
    posts=posts_dic.get('posts')
    paginas_totales=posts_dic.get('paginas_totales')


    formulario_contacto=FormularioContacto()

    return render(request, 'blog/blog.html', {"posts": posts, 'miFormulario':formulario_contacto, 
    "paginas_totales":paginas_totales, "pagina_activa":numero_pagina})

def buscar_blog(request):
    if request.method == 'POST':
        queryset=request.POST.get('buscar')
        if queryset:
            posts = Post.objects.filter(
                Q(titulo__icontains = queryset) |
                Q(contenido__icontains = queryset) 
            ).exclude(publicar=False).distinct()
        else:
            posts = Post.objects.filter(publicar=True)

    formulario_contacto=FormularioContacto()
    return render(request, 'blog/buscar_blog.html', {"posts": posts, 'miFormulario':formulario_contacto})
            
