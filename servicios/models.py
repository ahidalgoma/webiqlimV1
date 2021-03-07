from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50, help_text="Título del Servicio")
    ordenaparicion=models.IntegerField(verbose_name="Orden aparición", unique=True, help_text="Orden de aparición en la web")
    contenido=models.TextField(blank=True, null=True)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        ordering = ["ordenaparicion"]

    def __str__(self):
        return self.titulo
