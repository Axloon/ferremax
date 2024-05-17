from django.urls import path
from .views import home, contact, shop

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('shop/', shop, name="shop"),
]
