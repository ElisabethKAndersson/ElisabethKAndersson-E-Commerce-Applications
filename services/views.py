from django.shortcuts import render

# Create your views here.

def services(request):
    """ Presenting and selling services """

    return render(request, 'services/services.html')

def services_prices(request):
    """ Presenting and selling services """

    return render(request, 'services/services_prices.html')

def walks(request):
    """ Presenting and selling services """

    return render(request, 'services/walks.html')
