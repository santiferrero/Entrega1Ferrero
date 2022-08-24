# ProyectoCoder Santiago Ferero / Sofia Leviin

La pagina web creada, corresponde al Atelier PythonArt, un sitio donde los artistas suben sus obras para la venta, y los cliente crean un usuario para comprar las obras. Adicionalmente, los empleados tienen acceso a información relevante sobre ellos y sus compañeros.
La pagina de inicio esta definida por el archivo “inicio.py” donde se toma una de las visuales graficas de código abierto que nos ofrece Bootstrap.
La pagina de incio fue configurada con 3 vistas, según los interesados que pueden usarla: artistas, clientes y empleados.
Cada uno de estos 3 tipos de usuarios posee una vista especifica, y en cada una de estas vistas, se solicitan diferentes tipos de información.
De este modo, los nombres de las vistas (archivos) y los datos requeridos en cada vista, son los siguientes:
Artistas  formularioartistas  Nombre / Tipoarte / Subtipoarte
Clientes  formularioclientes  Nombre / Apellido / Email
Empleados  formularioempleados  Nombre / Apellido / Numeroempleado / Email / Area
Las urls correspondientes son:
localhost:8080/AppCoder/formularioartistas
localhost:8080/AppCoder/formularioclientes
localhost:8080/AppCoder/formularioempleados
Los templates usan herencia para que la visión grafica se mantenga aun cuando se navega a los distintos formularios.
Por otro lado, se configura el programa para que guarde los datos grabados en cada una de las vistas.
Por ultimo, se brinda la posibilidad de buscar datos (ya ingresados) para el caso de Artistas. Al ingresar datos de nombre, figuran los datos que ya han sido grabados anteriormente.
