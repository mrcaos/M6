from django.db import models

# Create your models here.
class Flan(models.Model):
    #ATRIBUTOS
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    
    #ATRIBUTO DE FECHA-HORA EN LA CREACION / cuando realice una insercion, insertara fecha y hora cuando se ingrese el registro de manera automatica
    created_at = models.DateTimeField(auto_now_add=True)
    
    #ATRIBUTO DE FECHA-HOTA EN LA MODIFICACION DE UN REGISTRO / actualiza el registro de fecha y hora en la modificacion para control y gestion
    updated_at = models.DateTimeField(auto_now=True)
    
    # deleted_at / se utiliza para eiminar un registro sin quitarlo de la tabla 
    
    def __str__(self) -> str:
        return f"Objeto Flan: {self.id} {self.name}"   #-> cabia el nombre enla admin de la web
    