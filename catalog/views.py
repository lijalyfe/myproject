from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})
