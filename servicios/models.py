from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50, help_text="Título del Servicio")
    contenido=models.TextField(blank=True, null=True)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo
