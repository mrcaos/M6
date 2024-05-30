"""
CREACION DE PYOYECTO

python -m venv onlyflans ---> creamos el entorno virtual

source onlyflans/Scritpt/activate ----> nos posicionamos en el proyecto

python -V ---> revisamos la version que tenemos instalada de python 

pip list ----> vemos la lista de ls paquetes

"python -m django version --> para ver la version de django "

pip install django ---> instala django y dependencias mas actuales
pip install django==3.2.4 instalad las versiones que buscamos django== version que buscamos

pip list ----> vemos las versiones instaladas

pip freeze > requirements.txt ---> verifica el respaldo "requirements.txt"

django-admin startproject onlyflans -----> generamos el proyecto , si tiene el mismo nombre del entorno virtual hacemos cd..  
creamos una carpeta x , entramos y generamos el startproject

cd/x cd/onlyflans --> entramos al proyecto

pip list -----> para revisar las versiones

pip freeze > requirements.txt ----->  verifica el respaldo "requirements.txt"

python manage.py migrate ------> genera las migraciones 

python manage.py runserver ----> proyecto ejecutado en el HTML http://127.0.0.1:8000/admin /admin desplega la creacion para el usuario

python manage.py createsuperuser  -----> creamos el super usuario y seguimos los datos 

CTRL+SHIFT+P buscaremos SQLite Open Database y veremos los usuarios y mas informacion, si queremos cambiar el nombre de la base de datos 
entraremos a settingss.py en el proyecto buscaremos DATABASE y en NAME despues del / pondreemos el nombre 'NAME': BASE_DIR / 'db.sqlite3'
ejemplo 'NAME': BASE_DIR / 'onliflans.sqlite3'

python manage.py startapp homeApp -----> creamos la aplicacion, agregamos la aplicacio en settings.py en las APPS agregarems "homeApp",

#en las views.py 
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

creamos la carpeta templates una vez creada llevamos el index.html o creamos en ella el index.html

iremos a la urls.py de el proyecto y importaremos 
from homeApp import views

path('', views.index, name='home') --> agregaremos el index 

deactivate --->  desactivas entorno y proyecto

"""