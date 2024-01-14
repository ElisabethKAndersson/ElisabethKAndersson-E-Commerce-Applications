from django.shortcuts import render

# Create your views here.


def shop(request):
    """ Index page """

    return render(request, 'shop/shop.html')
