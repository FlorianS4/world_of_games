from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
# Create your views here.


def checkout(request):
    bag = request.session.get('shoppingbag', {})
    if not bag:
        messages.error(request, "There's nothing in your shoppingbag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_puplic_key': 'pk_test_51QvFx6LfEdUMr3PoFyiiaMk0maDaaFYHiFBRfRbF4ZxX342GtF8KNKSCXbcL5ZYELi1W9xi3dyHvBrSFwa424U0700G0HzexkZ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
