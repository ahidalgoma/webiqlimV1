from django.db import models

# Create your models here.

class ParamWeb(models.Model):
    POSIBLES_VALORES=[('A','Antes'), ('D','Después'), ('N', 'No aparece')]
    POSIBLES_IDIOMAS=[('es-EU', 'Español-Europa'), ('en-EN', 'English-England')]
    idioma=models.CharField(max_length=5, help_text='Idioma de la web', choices=POSIBLES_IDIOMAS)
    mensaje_bienvenida=models.CharField(max_length=50, help_text="Mensaje de Bienvenida")
    subtitulo_bienvenida=models.CharField(max_length=50, help_text="Subtítulo de Bienvenida")
    titulo_menu=models.CharField(max_length=50, help_text="Título en el menú")
    titulo_hoja=models.CharField(max_length=50, help_text="Título en la página")
    contenido=models.TextField(blank=True, null=True)
    imagen=models.ImageField(upload_to='webiqlimapp')
    efecto_imagen=models.CharField(max_length=1, help_text="Lugar de aparición de la imagen", default="N", choices=POSIBLES_VALORES)
    activa=models.BooleanField(help_text="Si está activa esta será la que se publique")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='home'

    def __str__(self):
        return self.mensaje_bienvenida
