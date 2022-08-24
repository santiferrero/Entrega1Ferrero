from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Artistas, Clientes, Empleados
from AppCoder.forms import ArtistasFormulario, ClientesFormulario, EmpleadosFormulario

# Create your views here.


def inicio(request):
    return render(request, "AppCoder/inicio.html")


def artistas(request):
    return render(request, "AppCoder/artistas.html")


def clientes(request):
    return render(request, "AppCoder/clientes.html")


def empleados(request):
    return render(request, "AppCoder/empleados.html")


def fartistas(request):
    if request.method == "POST":

        miFormulario = ArtistasFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            artista = Artistas(nombre=informacion['nombre'], tipoArte=informacion['tipoArte'], subTipoArte=informacion['subTipoArte'])
            artista.save()
            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = ArtistasFormulario()
    return render(request, "AppCoder/formartistas.html", {"miFormulario": miFormulario})

def fclientes(request):
    if request.method == "POST":

        miFormulario = ClientesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Clientes(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            cliente.save()
            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = ClientesFormulario()
    return render(request, "AppCoder/formclientes.html", {"miFormulario": miFormulario})

def fempleados(request):
    if request.method == "POST":

        miFormulario = EmpleadosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empleado = Empleados(nombre=informacion['nombre'], apellido=informacion['apellido'], numeroEmpleado=informacion['numeroEmpleado'], email=informacion['email'], area=informacion['area'])
            empleado.save()
            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = EmpleadosFormulario()
    return render(request, "AppCoder/formempleados.html", {"miFormulario": miFormulario})


def busquedaNombre(request):
    artista = []
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        artista = Artistas.objects.filter(nombre__icontains=nombre)

    contexto = {
        'my_form': Artistas(),
        'artistas': artista
    }
    return render(request, "AppCoder/busquedaNombre.html", contexto)
