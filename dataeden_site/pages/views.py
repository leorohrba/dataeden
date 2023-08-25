# from django.contrib.auth.models import User
# import django
# from django.conf import settings
from django.http import HttpResponse#, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
# from django.urls import reverse #, resolve
# from django.utils.translation import activate
from dataeden_site.settings import STATIC_URL
from django.views.decorators.csrf import csrf_protect
from .forms import EmailForm, ContactForm
from .models import EmailAddress, ContactModel, LanguageManager
# from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Import the ratelimit decorator
# from brake.decorators import ratelimit
from django_ratelimit.decorators import ratelimit

def index(request, erro=None, email_form=EmailForm(prefix='email_form'), contact_form=ContactForm(prefix='contact_form')):
    LanguageManager.activate_language(request)  # Activate the appropriate language

    template = get_template('templates/index.html')
    context = {
        'title': 'Data Eden',
        'content': 'Welcome to Data Eden',
        'css_url': STATIC_URL + 'pages/style.css',
        'email_form': email_form,
        'contact_form': contact_form,
        'erro': erro,
    }
    return HttpResponse(template.render(context, request))

def success(request, method):

    LanguageManager.activate_language(request)  # Activate the appropriate language

    context = {
        'title': 'Data Eden',
        'content': 'Success!',
        'css_url': STATIC_URL + 'pages/style.css',
        'method': method,
        # 'full_url': request.build_absolute_uri(),
    }
    template_name = 'templates/success.html'
    return render(request, template_name, context)


def change_language(request):
    return LanguageManager.change_language(request)

@ratelimit(key='ip', rate='1/m')
@csrf_protect
@require_POST
def register_email(request): 
    LanguageManager.activate_language(request)  # Activate the appropriate language
    # print(request.LANGUAGE_CODE)
    form = EmailForm(request.POST)

    return EmailAddress.save_email(form)
    
def contact(request):
    LanguageManager.activate_language(request)  # Activate the appropriate language
    form = ContactForm(request.POST)
    return ContactModel.contact(request, form)


        
