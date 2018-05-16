from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

from nickWebDeploy import settings
from .models import businessCard as bizcard
from .forms import businessCardForm
from django.shortcuts import render

from django.contrib import messages
import urllib
import json

def home(request):
    template_name = 'homepage/porfolio.html'


    if request.method == 'POST':
        form = businessCardForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            email= request.POST.get("email")
            name = form.cleaned_data['contact_name']
            biz_name = form.cleaned_data['company']
            phone_number = form.cleaned_data['phone_number']
            message  = form.cleaned_data['message']

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''


            if result['success']:
                biz = bizcard(email=email, contact_name=name, company=biz_name, phone_number=phone_number,
                              message=message)

                biz.save()
                messages.success(request, 'Thank you for considering me ')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

        else:
            messages.warning(request, 'SomeThing went wrong')


    return render(request,template_name)