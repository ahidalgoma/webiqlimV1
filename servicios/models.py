from django.db import models

# Create your models here.

class Servicio(models.Model):
    POSIBLES_VALORES=[('P','Pequena'), ('M','Mediana'),]
    POSIBLES_FORMATOS=[('C','Circular'), ('N', 'Normal'),]
    titulo=models.CharField(max_length=50, help_text="Título del Servicio")
    ordenaparicion=models.IntegerField(verbose_name="Orden aparición", unique=True, help_text="Orden de aparición en la web")
    contenido=models.TextField(blank=True, null=True)
    imagen=models.ImageField(upload_to='servicios')
    efecto=models.CharField(max_length=1, help_text="Efecto de la imagen", default="P", choices=POSIBLES_VALORES)
    formato=models.CharField(max_length=1, help_text="Aparecera la imagen en cirulo o cuadrada-Normal", default="N", choices=POSIBLES_FORMATOS)
    eslogo=models.BooleanField(default=False, help_text="Si es logo no redirecciona a texto servicio")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        ordering = ["ordenaparicion"]

    def __str__(self):
        return self.titulo
