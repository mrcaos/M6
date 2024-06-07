"""
hito1
CREACION DE PYOYECTO

python -m venv onlyflans ---> creamos el entorno virtual

source onlyflans/Scritpt/activate ----> nos posicionamos en el proyecto

python -V ---> revisamos la version que tenemos instalada de python 

pip list ----> vemos la lista de ls paquetes

"python -m django version --> para ver la version de django "

pip install django ---> instala django y dependencias mas actuales
pip install django==3.2.4 instala la version que se pide"3.2.4" django== version que buscamos

pip list ----> vemos las versiones instaladas

pip freeze > requirements.txt ---> verifica el respaldo "requirements.txt"

django-admin startproject onlyflans -----> generamos el proyecto , si tiene el mismo nombre del entorno virtual hacemos cd..  
creamos una carpeta x , entramos y generamos el startproject

cd/x cd/onlyflans --> entramos al proyecto

pip list -----> para revisar las versiones

pip freeze > requirements.txt ----->  verifica el respaldo "requirements.txt"

python manage.py migrate ------> genera las migraciones 

python manage.py createsuperuser  -----> creamos el super usuario y seguimos los datos

python manage.py runserver ----> proyecto ejecutado en el HTML http://127.0.0.1:8000/admin /admin desplega la creacion para el usuario

CTRL+SHIFT+P buscaremos SQLite Open Database y veremos los usuarios y mas informacion, si queremos cambiar el nombre de la base de datos 
entraremos a settingss.py en el proyecto buscaremos DATABASE y en NAME despues del / pondreemos el nombre 'NAME': BASE_DIR / 'db.sqlite3'
ejemplo 'NAME': BASE_DIR / 'onliflans.sqlite3'

python manage.py startapp homeApp -----> creamos la aplicacion 


hito2
agregamos la aplicacion en settings.py del proyecto en las APPS agregarems "App", o como se llame nuestra APPs
asi crearemos las vistas y entregan las repspuestas atraves del templates welcome.html y asi, para reistrarlas vamos a url.py del proyecto
en las views.py de la homeApp 
from django.shortcuts import render

# Create your views here. ---> se obtine la respuesta de render especificando la pagina que utilizaremos
def welcome(request):
    return render(request,"welcome.html",{})

def about(request):
    return render(request,"about.html".)

def index(request):
    return render(request,"index.html")

creamos la carpeta templates en la App una vez creada llevamos el index.html o creamos en ella el index.html

iremos a la urls.py de el proyecto y importaremos la ruta
from homeApp import views

path('', views.index, name='home') --> ejemplo para importar nuevas vistas 

python manage.py runserver --> ya veriamos lo que vamos agregando 

ejemplo de generar una variable de contexto hacia el fron end, agregado en el return render(request,"index.html",context)
def index(request):
    context = {
        "nombre": "Juan",
        "apellido": "Aguilera"
    }
    return render(request,"index.html") / return render(request,"index.html".context)
    
    <!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
                integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
    

<h1>Hello, {{nombre}} {{apellido}}!</h1>  ----->asi capturamos la informacion del back end al front end 

    

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>

</html>


para gerar los templates y sus archivos html vamos al archivo url.py del proyecto y agregamos las rutas

from web.views import welcome,about,index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'), -----> templates de index
    path('about', about, name='about'), --->  templates de about
    path('welcome', welcome, name='welcome'), ----> templates de welcome
]


agregaremos statics a las plantillas asi agregaremos archivos css o javaScript 

crearemos una carpeta static en la app donde estan los templates y agregaremos css,img,js dentro de static 
dejaremos las imagenes del proyecto en img para poder aplicarlas en donde quieras
se agrega la etiqueta 

en el <head> agregaremos {% load ststic %} ----> asi cargara todo en static

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Indice</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
                integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">  ---> vinculamos los archivos css
    <script src="{% static 'js/script.js' %}"></script> ------> vinculamos los archivos javaScript
</head>

en el <body> ingregsaremos la ruta 

<body>
    <div class="container">
            <h1>Indice</h1>
            <img src="{% static 'img/onlyflans.png' %}" alt="onlyflans" width="50%"/>
        </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
                integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>

</html>

asi cargamos la informacion.

cuando inyectemos una plantilla o un componente tenemos que crear en templates espeificamente lo que vamos a crear ejemplo navbar.html y pegaremos de bootstrap un navbar,
en la html incluiremos el template de la paguina 

<body>

    {% block "navbar" %} ---> abrimos el bloque 
    {% include "navbar.html"%} ---> agregamos el bloque 
    {% endblock %} ---> cerramos el bloque

    <div class="container">
        <h1>Indice</h1>
    </div>

    {% block "footer" %}  ----> asi abrimos el footer o el bloque 
    {% include "footer.html"%} ---> agregamos el bloque
    {% endblock %} ----> cerramos el bloque 

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>

</html>

cualquier cabio de distribucion de los HTML se hacen en cada seccion footer.html, navbar.html etc
aca los estamos agregando a la paguina runserver 


hito3
source onlyflans/Scripts/activate ---> siempreactivar el proyecyo






deactivate --->  desactivas entorno y proyecto

"""
