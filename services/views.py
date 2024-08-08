from django.shortcuts import render
from .models import Service

# Create your views here.

def services_presentation(request):
    """ Presenting services """

    return render(request, 'services/services_presentation.html')

def services_prices(request):
    """ Prices and memberships """

    services = Service.objects.all()
    print("Services:", services) 

    context = {
        'services': services,
    }

    return render(request, 'services/services_prices.html', context)

def walks(request):
    """ Information about senior walks """

    return render(request, 'services/walks.html')
