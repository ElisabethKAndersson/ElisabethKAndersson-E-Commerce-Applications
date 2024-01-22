from django.shortcuts import render

# Create your views here.

def services(request):
    """ Presenting services """

    return render(request, 'services/services.html')

def services_prices(request):
    """ Prices and memberships """


    context = {
        'services': services,
    }

    return render(request, 'services/services_prices.html')

def walks(request):
    """ Information about senior walks """

    return render(request, 'services/walks.html')
