from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import GameProduct

# Create your views here.


def all_products(request):
    """a view to show products, sorting and search queries"""
    products = GameProduct.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria was entered!")
                return redirect(reverse('products'))

            queries = Q(product_name__icontains=query) | Q(product_description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """view to show a single product"""
    product = get_object_or_404(GameProduct, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
