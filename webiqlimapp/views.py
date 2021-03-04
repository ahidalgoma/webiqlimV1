from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'webiqlimapp/home.html')

def servicios(request):
    return render(request, 'WebIqlimApp/servicios.html')

