from django import forms
from captcha.fields import CaptchaField

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", max_length=100, required=True)
    email=forms.CharField(label="Email", max_length=100, required=True)
    contenido=forms.CharField(label="Contenido", max_length=255, widget=forms.Textarea)
    captcha=CaptchaField()



