from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('', views.inicio), #esta era nuestra primer view
    path('artistas', views.artistas, name="Artistas"),
    path('clientes', views.clientes, name= "Clientes"),
    path('empleados', views.empleados, name= "Empleados"),
    path('formularioartistas', views.fartistas),
    path('formularioclientes', views.fclientes),
    path('formularioempleados', views.fempleados),
    path('busquedaNombre', views.busquedaNombre, name= "BusquedaNombre"),
]

