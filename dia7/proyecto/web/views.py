from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def about(request):
    return render(request,"about.html")

def index(request):
    return render(request,"index.html")