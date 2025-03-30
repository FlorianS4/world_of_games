from django.shortcuts import render
from .models import GameProduct

# Create your views here.


def all_products(request):
    """a view to show products, sorting and search queries"""
    products = GameProduct.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
