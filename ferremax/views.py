from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'ferremax/home.html')

def contact(request):
    return render(request, 'ferremax/contact.html')

def shop(request):
    return render(request, 'ferremax/shop.html')