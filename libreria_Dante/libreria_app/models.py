
from tabnanny import verbose
from django.db import models


# Create your models here.
    
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    Titulo=models.CharField(max_length=300,verbose_name='Titulo')
    Autor=models.CharField(max_length=200,verbose_name='Autor')
    Numero_Paginas=models.IntegerField(verbose_name='N_Paginas')
    Genero=models.CharField(max_length=500,verbose_name='Genero')
    Leido=models.BooleanField(verbose_name='Leido',default=True)
    Imagen=models.ImageField(upload_to='Img_Books',null=True,blank=True)

    def __str__(self):
        return str("{}".format(self.Titulo))

    def delete(self,using=None,keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()

class ImportantPoints(models.Model):
    id=models.AutoField(primary_key=True)    
    Titulo_Libro=models.ForeignKey(Book,on_delete=models.CASCADE,default="")
    Apunte=models.TextField(verbose_name='Apunte',null=True)    

    def __str__(self):
        return str("Id: {} - Titulo Libro: {}".format(self.id,self.Titulo_Libro))

class WishList(models.Model):
    id=models.AutoField(primary_key=True)
    Titulo_Libro=models.CharField(max_length=300,verbose_name='Titulo_libro')
    Precio=models.IntegerField(verbose_name='Precio')
    Imagen=models.ImageField(upload_to='Img_Books',null=True,blank=True)
   
    def __str__(self):
         return str("Titulo Libro: {} - Precio: {}".format(self.Titulo_Libro,self.Precio))
   
    def delete(self,using=None,keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()