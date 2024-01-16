from django.shortcuts import render

# Create your views here.

def services(request):
    """ Presenting and selling services """

    return render(request, 'services/services.html')