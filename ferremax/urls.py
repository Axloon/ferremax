from django.urls import path, include
from .views import home, contact, shop, cart, add_to_cart, increase_quantity, decrease_quantity, remove_from_cart, init_payment, payment_success, ProductoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
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