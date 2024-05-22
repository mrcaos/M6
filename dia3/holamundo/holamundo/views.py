from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse("""
    <h1>Hola Mundo!!!</h1>
    <p>Esta es mi primera aplicación con Django mostrando HTML</p>
    """)


def test(request):
        return HttpResponse("""
            <h1>Esta es otra pagina</h1>
            <p>este es otro parrafo</p>
            <img src="" alt="imagen de prueba"
        """)