from django.shortcuts import render

# Create your views here.


def view_shopping_bag(request):
    """A view to show the shopping bags content"""

    return render(request, 'shoppingbag/shopping_bag.html')
