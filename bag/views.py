from django.shortcuts import render


# Create your views here.


def bag(request):
    """ Shopping bag """

    return render(request, 'bag/bag.html')
