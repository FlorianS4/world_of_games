from django.shortcuts import render, redirect

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
