from django.urls import path, include
from .views import home, registro, conversor, contact, shop, cart, add_to_cart, increase_quantity, decrease_quantity, remove_from_cart, init_payment, payment_success, payment_failed, ProductoViewSet, VendedorViewSet, BodegueroViewSet, home_vendedor, home_bodeguero, home_contador, productos_vendedor, ordenes_vendedor, ProductosDisponiblesView, AprobarRechazarPedidosView, OrganizarDespachoView, VerOrdenesView, PrepararPedidosView, EntregarPedidosView
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('producto', ProductoViewSet),
router.register('vendedor', VendedorViewSet),
router.register('bodeguero', BodegueroViewSet),


urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('ferremax/vendedor', home_vendedor, name="home_vendedor"),
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
    path('payment_failed/', payment_failed, name='payment_failed'),
    path('api/', include(router.urls)),
    path('vendedor/productos_disponibles/', ProductosDisponiblesView.as_view(), name='productos_disponibles'),
    path('vendedor/aprobar_rechazar_pedidos/', AprobarRechazarPedidosView.as_view(), name='aprobar_rechazar_pedidos'),
    path('vendedor/organizar_despacho/', OrganizarDespachoView.as_view(), name='organizar_despacho'),
    path('bodeguero/ver_ordenes/', VerOrdenesView.as_view(), name='ver_ordenes'),
    path('preparar_pedidos/<int:pedido_id>/', PrepararPedidosView.as_view(), name='preparar_pedidos'),
    path('entregar_pedidos/<int:pedido_id>/', EntregarPedidosView.as_view(), name='entregar_pedidos'),
]