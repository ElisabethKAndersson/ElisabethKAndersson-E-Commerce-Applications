from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product
from services.models import Service


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })


    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context

def bag_service_contents(request):

    bag_service_items = []
    total = 0
    product_count = 0
    service_bag = request.session.get('service_bag', {})

    for service_id, quantity in bag.service():
        service = get_object_or_404(Service, pk=service_id)
        total += quantity * servicet.price
        service_count += quantity
        bag_service_items.append({
            'service_id': service_id,
            'quantity': quantity,
            'service': service,
        })


    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + total

    context = {
        'bag_service_items': bag_service_items,
        'total': total,
        'service_count': service_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context