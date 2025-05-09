from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import GameProduct


def shoppingbag_contents(request):
    """
    Context processor for shoppingbag contents
    """
    shoppingbag_items = []
    total = 0
    product_count = 0
    shoppingbag = request.session.get('shoppingbag', {})

    for item_id, item_data in shoppingbag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(GameProduct, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            shoppingbag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

        else:
            product = get_object_or_404(GameProduct, pk=item_id)
            for game_type, quantity in item_data['items_by_game_type'].items():
                total += quantity * product.price
                product_count += quantity
                shoppingbag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'game_type': game_type,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
