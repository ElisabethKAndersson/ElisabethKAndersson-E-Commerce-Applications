from django.shortcuts import render

# Create your views here.


def contact(request):
    """ Index page """

    return render(contact, 'contact/contact.html')
