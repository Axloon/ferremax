from django.shortcuts import render
from .models import Producto
from rest_framework import viewsets
from .serializer import ProductoSerializer

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



def home(request):
    return render(request, 'ferremax/home.html')

def contact(request):
    return render(request, 'ferremax/contact.html')

def shop(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'ferremax/shop.html', data)