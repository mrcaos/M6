from django.shortcuts import render
#siempre importar los modelos 
from .models import Flan
from .form import LoginForm

# Create your views here.

def index(request):
    #select * from web_flan; --> tipo de consulta pero no lo utilizaremos ahora ocuparemos
    flanes = Flan.objects.all()
    
    #es un where
    flanes_publicos = Flan.objects.filter(is_private=False) 

    
    context = {
        'flanes': flanes_publicos
    }
    
    return render(request,"index.html",context)

def welcome(request):
    request.session['name']="Juan"
    flanes_privados = Flan.objects.filter(is_private=True)
    
    context = {
        'flanes': flanes_privados
    }
    
    return render(request,"welcome.html",context)

def about(request):
    return render(request,"about.html",{})

def contacto(request):
    if request.method =="GET":
        return render(request,"contacto.html")
    
    if request.method =="POST":
        email = request.POST["email"]
        nombre = request.POST["nombre"]
        mensaje = request.POST["mensaje"]
        
        return render(request,"contacto.html")
    
def login(request):
    if request.method =="GET":
        return render(request,"login.html")
    
    else:
        email = request.POST["email"]
        password = request.POST["password"]
        
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            LoginForm.objects.create(**form.cleaned_data)
            
            
            
        return redirect('welcome')