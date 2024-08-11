from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    age_yes = forms.BooleanField(label='I verify that I am 65 years old or older')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user