from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def bienvenida(request):
    return render(request, 'bienvenida.html')

@login_required
def home(request):
    if request.user.profile.is_docente:
        # Muestra la página para docentes
        return render(request, 'home_docente.html')
    elif request.user.profile.is_estudiante:
        # Muestra la página para estudiantes
        return render(request, 'home_estudiante.html')
    else:
        # Muestra una página genérica si no se define el tipo
        return render(request,'/acceso_denegado/')
    
def acceso_denegado(request):
    return render(request,'acceso_denegado.html')

def login(request):
    return render(request, 'login.html')

