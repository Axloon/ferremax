from django.urls import path, include
from .views import home, contact, shop, add_to_cart, cart_view, ProductoViewset, conversor
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('shop/', shop, name="shop"),
    path('add_to_cart/<int:producto_id>/', add_to_cart, name="add_to_cart"),
    path('cart/', cart_view, name="cart"),
    path('conversor/', conversor, name="conversor"),
    path('api/', include(router.urls)),
    
]
