from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    disponible = models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre
    
class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    aconfirmar = models.BooleanField()
    descripcion = models.TextField()
    
    
    def __str__(self):
        return self.nombre
    
class Bodeguero(models.Model):
    nombre = models.CharField(max_length=100)
    aceptar = models.BooleanField()
    
    def __str__(self):
        return self.nombre