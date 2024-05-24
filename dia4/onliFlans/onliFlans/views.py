from django.shortcuts import render
from django.http import HttpResponse

def home(request):
        return HttpResponse("""
            <!DOCTYPE html>
            <html lang="en">

        <head>
            <title>OnliFlans</title>
            <meta name="author" content="Juan Aguilera Duhalde" />
            <meta name="description" content="Una empresa enfocada en el mundo de la pastelería y los postres" />
            <meta name="keywords" content="Santiago de Chile, Providencia, Empresa Familiar, Productos de Calidad," />
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
                        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>

        <body>
            
            <nav class="navbar navbar-expand-lg fixed-top px-3" data-bs-theme="dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">
                        <img src="assets/img/of.png" alt="OnliFlans" width="32px">
                        OnliFlans
                    </a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                        data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                        aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="#inicio">Inicio</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#quienes_somos">Quienes Somos</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#destacados">Destacados</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#contacto">Contacto</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <header id="inicio">
                <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="assets/img/love.jpg" class="d-block w-100" alt="love1">
                        </div>
                        <div class="carousel-item">
                            <img src="assets\img\pasteles.jpg" class="d-block w-100" alt="pasteles2">
                        </div>
                        <div class="carousel-item">
                            <img src="assets/img/tortas.jpg" class="d-block w-100" alt="tortas3">
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying"
                        data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying"
                        data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </header>


            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
                    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" 
                    crossorigin="anonymous"></script>
        </body>

        </html>                

        """)
        
        
def contacto(request):
        return HttpResponse("""
                <!DOCTYPE html>
                <html lang="en">

        <head>
            <title>OnliFlans</title>
            <meta name="author" content="Juan Aguilera Duhalde" />
            <meta name="description" content="Una empresa enfocada en el mundo de la pastelería y los postres" />
            <meta name="keywords" content="Santiago de Chile, Providencia, Empresa Familiar, Productos de Calidad," />
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
                        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        
        <body>
        
            <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Email address</label>
                    <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
            </div>
            <div class="mb-3">
                    <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
            </div>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" 
            crossorigin="anonymous"></script>    
        </body>
        
        </html>
                            
        """)