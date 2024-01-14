from django.shortcuts import render

# Create your views here.


def contact(request):
    """ Contact page """

    return render(request, 'contact/contact.html')
