from django import forms
from django.shortcuts import render, HttpResponse, redirect
from contacto.forms import FormularioContacto
from django.core.mail import EmailMessage
import os
from dotenv import load_dotenv

def enviocorreo(nombre, email, contenido):
    load_dotenv()
    email=EmailMessage("Mensaje desde la web de Iqlim",
    "el usuario con nombre {} con el mail {} escribe: \n\n {}".format(nombre, email,contenido),
    os.getenv('CO_MAIL'),[os.getenv('CO_MAIL')],reply_to=[email])

    try:
        email.send()
        return True
    except:
        return False
