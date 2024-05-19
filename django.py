"""
paso previo ver si tenfo DJANGO
pip list (window) ----> Django   5.0.6
pip3 list (mac,linux)

pip install django

Etapa 1 preparacion del entorno virtual e instalacion de depencencias 
Paso 1 habilitar entorno virtual con python:

python -m venv nombre_entorno
python -m venv vdjango

Paso 2 en la carpeta generada vdjango, veremos un subdiretor llamADO Scripts.

.\vdjango\Scripts\activate (win)
call vdjango\Scripts\activate
source vdjango/Scripts/activate ---> valido

la crecion del entorno es para crear proyetos con librerias especificas 


Paso 3: Instalamos Django con el siguiente comando pip install django

Paso 4: Creamos el proyecto en Django con el siguiente comando
django-admin startproject myFirstApp
django-admin startproject nombre_proyeco

Paso 5.1: Accedemos al directorio myFirstApp desde la consola
cd myFirstApp

Paso 5.2: ejecutamos el 
siguiente comando para levantar el servidor web y ver nuestro proyecto en el 
navegador.
python manage.py runserver

deactivate #desactiva el entorno virtual
"""
"""DEAFIO GUIADO DIA 1

python -m venv ferreteria
source ferreteria/Scripts/activate
pip install django==3.2.4
pip list
pip freeze > requirements-ferreteria.txt

python -m venv laesquina
source laesquina/Scripts/activate
pip install django<3
pip install django==2.2
pip list
pip freeze > requirements-laesquina.txt

python -m venv onlyflans
source onlyflans/Scripts/activate
pip install django==3.2
pip list
pip freeze > requirements-onlyflans.txt

python -m venv prestobar
source prestobar/Scripts/activate
pip install astral
pip list
pip freeze > requirements-prestobar.txt

python -m venv taller
source taller/Scripts/activate
pip install pytz==2019.3
pip list
pip freeze > requirements-taller.txt

python -m venv calendariolunar
source calendariolunar/Scripts/activate
pip install -r requirements.txt
pip list
pip freeze > requirements-calendariolunar.txt
"""


"""CREACION DE ENTORNO CON CONDA 
    Provee al menos 4 comandos que utilizaremos con frecuencia:
    
● conda create --name nombre_entorno: Crea un nuevo entorno virtual.

● conda activate nombre_entorno: Activa un entorno virtual.

● conda deactivate: Desactiva el entorno virtual actual.

● conda env list o conda info --envs: Lista los entornos virtuales

"""
