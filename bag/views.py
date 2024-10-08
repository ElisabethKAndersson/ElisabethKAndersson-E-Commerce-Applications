from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity  

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity if product. """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id) == quantity

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove product from bag"""

    try:

        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['service_bag'] = service_bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)

def add_service_to_bag(request, service_id):
    """ Add service to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    service_bag = request.session.get('service_bag', {})

    if service_id in list(service_bag.keys()):
        service_bag[service_id] += quantity
    else:
        service_bag[service_id] = quantity
    
    request.session['service_bag'] = service_bag
    print(service_bag)
    return redirect(redirect_url)