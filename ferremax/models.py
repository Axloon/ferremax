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
    
class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('en_preparacion', 'En Preparación'),
        ('entregado', 'Entregado')
    ]
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.producto.nombre}"