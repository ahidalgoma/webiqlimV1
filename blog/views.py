from django.shortcuts import render, HttpResponse, redirect
from webiqlimapp.forms import FormularioContacto
from webiqlimapp.funciones.enviocorreo import enviocorreo
from .models import Post
from datetime import date

# Create your views here.

pagina_activa=1

def blog(request):
    posts=[]
# Se calcula el numero de paginas que debe aparecer en el pie
    paginas_totales=round(Post.objects.all().count()/3)
    if Post.objects.all().count()/3 > paginas_totales:
        paginas_totales+=1
# --------------
    posicion_desde=0
    posicion_hasta=0
    if request.method=="GET":
        if "pagina" in request.GET:
#        posicion_desde=request.GET.find("pagina")
#        posicion_hasta=request.GET.find(": [", posicion_desde+6)
            posicion_desde=1
            posicion_hasta=2
#        pagina_activa=int(request.GET[7:len(request.GET)])

    posts=cargar_tabla(posts, pagina_activa)    


    if request.method=="POST":
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")            
            if enviocorreo(nombre, email, contenido):
                return redirect ('/blog/?valido')
            else:
                return redirect ('/blog/?NOenvio')
        else:
           return redirect ('/blog/?NOcorrectoscampos')
    else:
        formulario_contacto=FormularioContacto()

    return render(request, 'blog/blog.html', {"posts": posts, 'miFormulario':formulario_contacto, 
    "paginas_totales":paginas_totales, "pagina_activa":pagina_activa, "posicion_desde":posicion_desde,
    "posicion_hasta":posicion_hasta})


def verblog(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")            
            if enviocorreo(nombre, email, contenido):
                return redirect ('/blog/?valido')
            else:
                return redirect ('/blog/?NOenvio')
        else:
           return redirect ('/blog/?NOcorrectoscampos')
    else:
        formulario_contacto=FormularioContacto()

    return render(request, 'blog/VerBlog.html', {"post": post, 'miFormulario':formulario_contacto})

def cargar_tabla(posts, pagina_inicio):
    if pagina_inicio != 1:
        fila_inicio=((pagina_inicio-1)*3)+1
    else:
        fila_inicio=1
    posts = Post.objects.all()[fila_inicio-1:fila_inicio+2]
    return posts

