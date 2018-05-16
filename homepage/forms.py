
from django import forms



class businessCardForm(forms.Form):
    email = forms.CharField(max_length=255)
    contact_name = forms.CharField(max_length=255, required=False)
    company = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=255,required=False)
    message = forms.CharField(max_length=255,required=False)