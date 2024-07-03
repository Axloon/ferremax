from django.urls import path, include
from .views import home, conversor, contact, shop, cart, add_to_cart, increase_quantity, decrease_quantity, remove_from_cart, init_payment, payment_success, ProductoViewSet, home_vendedor, home_bodeguero, home_contador, productos_vendedor, ordenes_vendedor
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('ferremax/vendedor', home_vendedor, name="home_vendedor"),
    path('productos_vendedor', productos_vendedor, name="productos_vendedor"),
    path('ordenes_vendedor', ordenes_vendedor, name="ordenes_vendedor"),
    path('ferremax/bodeguero', home_bodeguero, name="home_bodeguero"),
    path('ferremax/contador', home_contador, name="home_contador"),
    path('contact/', contact, name="contact"),
    path('currency_converter/', views.currency_converter, name='currency_converter'),
    path('conversor/', conversor, name="conversor"),
    path('shop/', shop, name="shop"),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('increase_quantity/<int:product_id>/', increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:product_id>/', decrease_quantity, name='decrease_quantity'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('init_payment/', init_payment, name='init_payment'),
    path('payment_success/', payment_success, name='payment_success'),
    path('api/', include(router.urls)),
]