from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import GameProduct


# Create your views here.


def view_shoppingbag(request):
    """A view to show the shopping bags content"""

    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_shoppingbag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(GameProduct, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    game_type = None
    if 'product_game_type' in request.POST:
        game_type = request.POST['product_game_type']
    shoppingbag = request.session.get('shoppingbag', {})

    if game_type:
        if item_id in list(shoppingbag.keys()):
            if game_type in shoppingbag[item_id]['items_by_game_type'].keys():
                shoppingbag[item_id]['items_by_game_type'][game_type] += quantity
                messages.success(request, f'Updated game type {game_type.upper()} {product.product_name} to {shoppingbag[item_id]["items_by_game_type"][game_type]}')
            else:
                shoppingbag[item_id]['items_by_game_type'][game_type] = quantity
                messages.success(request, f'Added game type {game_type.upper()} {product.product_name} to your shoppingbag')
        else:
            shoppingbag[item_id] = {'items_by_game_type': {game_type: quantity}}
            messages.success(request, f'Added game type {game_type.upper()} {product.product_name} to your shoppingbag')
    else:
        if item_id in list(shoppingbag.keys()):
            shoppingbag[item_id] += quantity
            messages.success(request, f'Updated {product.product_name} quantity to {shoppingbag[item_id]}')
        else:
            shoppingbag[item_id] = quantity
            messages.success(request, f'Added {product.product_name} to your shoppingbag')

    request.session['shoppingbag'] = shoppingbag
    return redirect(redirect_url)


def adjust_shoppingbag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(GameProduct, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    game_type = None
    if 'product_game_type' in request.POST:
        game_type = request.POST['product_game_type']
    shoppingbag = request.session.get('shoppingbag', {})

    if game_type:
        if quantity > 0:
            shoppingbag[item_id]['items_by_game_type'][game_type] = quantity
            messages.success(request, f'Updated game type {game_type.upper()} {product.product_name} quantity to {shoppingbag[item_id]["items_by_game_type"][game_type]}')
        else:
            del shoppingbag[item_id]['items_by_game_type'][game_type]
            if not shoppingbag[item_id]['items_by_game_type']:
                shoppingbag.pop(item_id)
                messages.success(request, f'Removed game type {game_type.upper()} {product.product_name} from your shoppingbag')
    else:
        if quantity > 0:
            shoppingbag[item_id] = quantity
            messages.success(request, f'Updated {product.product_name} quantity to {shoppingbag[item_id]}')
        else:
            shoppingbag.pop(item_id)
            messages.success(request, f'Removed {product.product_name} from your shoppingbag')

    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_shoppingbag'))


def remove_from_shoppingbag(request, item_id):
    """ Remove the item from the shopping bag """

    product = get_object_or_404(GameProduct, pk=item_id)

    try:
        game_type = None
        if 'product_game_type' in request.POST:
            game_type = request.POST['product_game_type']
        shoppingbag = request.session.get('shoppingbag', {})

        if game_type:
            del shoppingbag[item_id]['items_by_game_type'][game_type]
            if not shoppingbag[item_id]['items_by_game_type']:
                shoppingbag.pop(item_id)
            messages.success(request, f'Removed game type {game_type.upper()} {product.product_name} from your shoppingbag')
        else:
            shoppingbag.pop(item_id)
            messages.success(request, f'Removed {product.product_name} from your shoppingbag')

        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
