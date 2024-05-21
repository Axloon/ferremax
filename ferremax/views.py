from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from rest_framework import viewsets
from .serializer import ProductoSerializer
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType
from django.conf import settings

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
    token = request.GET.get('token_ws')
    transaction = Transaction(WebpayOptions(
        commerce_code=settings.TRANSBANK['COMMERCE_CODE'],
        api_key=settings.TRANSBANK['API_KEY'],
        integration_type=IntegrationType.TEST  # Cambiar a IntegrationType.LIVE en producción
    ))
    response = transaction.commit(token=token)
    if response['status'] == 'AUTHORIZED':
        # Aquí puedes procesar la orden como pagada
        request.session['cart'] = {}  # Vaciar el carrito después de la compra exitosa
        return render(request, 'payment_success.html', {'response': response})
    else:
        return render(request, 'payment_failed.html', {'response': response})