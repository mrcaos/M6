from django.shortcuts import render
#siempre importar los modelos 
from .models import Flan

# Create your views here.

def index(request):
    #select * from web_flan; --> tipo de consulta pero no lo utilizaremos ahora ocuparemos
    flanes = Flan.objects.all() 
    
    print(flanes)
    
    return render(request,"index.html",{})

def welcome(request):
    request.session['name']="Juan"
    return render(request,"welcome.html",{})

def about(request):
    return render(request,"about.html",{})

