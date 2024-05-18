from django.urls import path, include
from .views import home, contact, shop, ProductoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)


urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('shop/', shop, name="shop"),
    path('api/', include(router.urls)),
]
