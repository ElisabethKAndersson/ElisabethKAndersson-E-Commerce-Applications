from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PUZa5Dib5yNC9z0OVdnu1XqPstH7Dzc4Qg8Imv17WH1SjcGrQiyIlZxxU3QEw3UOYgwNOvnsD0mwhckeo0MxqdA00aD5TS5RG',
    }

    return render(request, template, context)