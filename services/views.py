from django.shortcuts import render

# Create your views here.

def services(request):
    """ Index page """

    return render(request, 'services/services.html')