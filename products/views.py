from django.shortcuts import render, get_object_or_404
from .models import GameProduct

# Create your views here.


def all_products(request):
    """a view to show products, sorting and search queries"""
    products = GameProduct.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """view to show a single product"""
    product = get_object_or_404(GameProduct, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
