from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "nombre": "Juan",
        "apellido": "Aguilera",
        
    }
    return render(request,"index.html")