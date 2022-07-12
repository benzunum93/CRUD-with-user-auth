from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Libro(models.Model):
    id=         models.AutoField(primary_key=True)
    titulo=     models.CharField(max_length=100, verbose_name='Titulo',null=True)
    imagen=     models.ImageField(upload_to='imagenes/',null=True,blank=True)
    descripcion=models.TextField(verbose_name='Descripción',null=True)

    def __str__(self):
        
        fila="Titulo: "+ self.titulo +" - "+ "Descripción: " + self.descripcion
        return fila

    def delete(self, using= None, keep_parents= False):

        self.imagen.storage.delete(self.imagen.name) #Para eliminar las imagenes adicional al contenido
        super().delete()