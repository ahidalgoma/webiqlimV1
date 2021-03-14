from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50, help_text="Nombre de la categoria")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    POSIBLES_VALORES=[('A','Antes'), ('P','Posterior'), ('I','Izquierda'), ('D', 'Derecha'), ('N', 'No aparece')]
    titulo=models.CharField(max_length=50, help_text="Título del Post")
    publicar=models.BooleanField(help_text="Una vez marcado aparecera en la web")
    contenido=models.TextField(blank=True, null=True)
    imagen=models.ImageField(upload_to='blog')
    efecto_imagen=models.CharField(max_length=1, help_text="Lugar de aparición de la imagen al ver el post", default="N", choices=POSIBLES_VALORES)
    autor=models.ForeignKey(User, on_delete=models.CASCADE) 
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
        ordering = ["-created"]

    def __str__(self):
        return self.titulo