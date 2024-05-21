from django.shortcuts import render, redirect
from .models import Producto
from rest_framework import viewsets
from .serializer import ProductoSerializer


# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        productos = Producto.objects.all()
        
        nombre = self.request.GET.get('nombre')
        
        if nombre:
            productos = productos.filter(nombre__contains=nombre)
            
        return productos

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

def add_to_cart(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    cart = request.session.get('cart', {})

    if producto_id in cart:
        cart[producto_id]['quantity'] += 1
    else:
        cart[producto_id] = {
            'name': producto.nombre,
            'price': producto.precio,
            'quantity': 1,
            'image': producto.imagen.url if producto.imagen else ''
        }

    request.session['cart'] = cart
    return redirect('shop')

def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'ferremax/cart.html', {'cart': cart, 'total': total})

def conversor(request):
    return render(request, 'ferremax/conversor.html')