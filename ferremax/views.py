from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Vendedor, Bodeguero
from rest_framework import viewsets
from .serializer import ProductoSerializer, VendedorSerializer, BodegueroSerializer
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType
from django.conf import settings
from .forms import ConversionForm
from .utils import clp_to_usd_conversion, usd_to_clp_conversion

# Crear tu vista aquí

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        return productos
    
class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

    def get_queryset(self):
        vendedor = Vendedor.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            vendedor = vendedor.filter(nombre__contains=nombre)

        return vendedor
    
class BodegueroViewSet(viewsets.ModelViewSet):
    queryset = Bodeguero.objects.all()
    serializer_class = BodegueroSerializer

    def get_queryset(self):
        bodeguero = Bodeguero.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            bodeguero = bodeguero.filter(nombre__contains=nombre)

        return bodeguero


def home(request):
    return render(request, 'ferremax/home.html')

def home_vendedor(request):
    return render(request, 'ferremax/vendedor/home_vendedor.html')

def home_bodeguero(request):
    return render(request, 'ferremax/bodeguero/home_bodeguero.html')

def home_contador(request):
    return render(request, 'ferremax/contador/home_contador.html')

def currency_converter(request):
    result = None
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            direction = form.cleaned_data['direction']
            if direction == 'CLP to USD':
                result = clp_to_usd_conversion(amount)
                result = f'{amount} CLP son {result:.2f} USD' if result else 'Error en la conversión'
            else:
                result = usd_to_clp_conversion(amount)
                result = f'{amount} USD son {result} CLP' if result else 'Error en la conversión'
    else:
        form = ConversionForm()
    return render(request, 'ferremax/currency_converter.html', {'form': form, 'result': result})

def conversor(request):
    return render(request, 'ferremax/conversor.html')

def contact(request):
    return render(request, 'ferremax/contact.html')


def shop(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'ferremax/shop.html', data)


def cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'ferremax/cart.html', {'cart': cart, 'total': total})


def add_to_cart(request, product_id):
    producto = get_object_or_404(Producto, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': producto.nombre,
            'price': producto.precio,
            'quantity': 1,
            'image': producto.imagen.url if producto.imagen else ''
        }

    request.session['cart'] = cart
    return redirect('cart')


def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
        request.session['cart'] = cart

    return redirect('cart')


def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart and cart[str(product_id)]['quantity'] > 1:
        cart[str(product_id)]['quantity'] -= 1
        request.session['cart'] = cart

    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart

    return redirect('cart')


def init_payment(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    transaction = Transaction(WebpayOptions(
        commerce_code=settings.TRANSBANK['COMMERCE_CODE'],
        api_key=settings.TRANSBANK['API_KEY'],
        integration_type=IntegrationType.TEST  # Cambiar a IntegrationType.LIVE en producción
    ))
    response = transaction.create(
        buy_order='12345678',  # Debe ser único por cada transacción
        session_id='your_session_id',
        amount=total,
        return_url=request.build_absolute_uri('/payment_success/')
    )
    request.session['transaction_token'] = response['token']
    return redirect(response['url'] + '?token_ws=' + response['token'])

def payment_success(request):
    return render(request, 'ferremax/payment_success.html')

def payment_failed(request):
    return render(request, 'ferremax/payment_failed.html')

def productos_vendedor(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'ferremax/vendedor/productos_vendedor.html', data)

def ordenes_vendedor(request):
    return render(request, 'ferremax/vendedor/ordenes_vendedor.html')