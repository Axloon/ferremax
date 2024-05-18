from django.shortcuts import render
from .models import Producto

# Create your views here.

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