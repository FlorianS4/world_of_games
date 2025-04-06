from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_shoppingbag(request):
    """A view to show the shopping bags content"""

    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_shoppingbag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

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
            else:
                shoppingbag[item_id]['items_by_game_type'][game_type] = quantity
        else:
            shoppingbag[item_id] = {'items_by_game_type': {game_type: quantity}}
    else:
        if item_id in list(shoppingbag.keys()):
            shoppingbag[item_id] += quantity
        else:
            shoppingbag[item_id] = quantity

    request.session['shoppingbag'] = shoppingbag
    return redirect(redirect_url)


def adjust_shoppingbag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    game_type = None
    if 'product_game_type' in request.POST:
        game_type = request.POST['product_game_type']
    shoppingbag = request.session.get('shoppingbag', {})

    if game_type:
        if quantity > 0:
            shoppingbag[item_id]['items_by_game_type'][game_type] = quantity
        else:
            del shoppingbag[item_id]['items_by_game_type'][game_type]
            if not shoppingbag[item_id]['items_by_game_type']:
                shoppingbag.pop(item_id)
    else:
        if quantity > 0:
            shoppingbag[item_id] = quantity
        else:
            shoppingbag.pop(item_id)

    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_shoppingbag'))


def remove_from_shoppingbag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        game_type = None
        if 'product_game_type' in request.POST:
            game_type = request.POST['product_game_type']
        shoppingbag = request.session.get('shoppingbag', {})

        if game_type:
            del shoppingbag[item_id]['items_by_game_type'][game_type]
            if not shoppingbag[item_id]['items_by_game_type']:
                shoppingbag.pop(item_id)
        else:
            shoppingbag.pop(item_id)

        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
