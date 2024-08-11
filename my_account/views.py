from django.shortcuts import render

# Create your views here.'

def age_modal(request):
    
    return render(request, 'my_account/age_modal.html')
