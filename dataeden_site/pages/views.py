# from django.contrib.auth.models import User
import django
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
# from dataeden_site.dataeden_site.settings import LANGUAGE_MAP
from dataeden_site.settings import STATIC_URL
from .forms import EmailForm, ContactForm
from django.core import mail
from django.template.defaultfilters import mark_safe
# from django.views.i18n import set_language
# from rosetta.utils import i18n as rosetta_i18n
from django.utils import translation
# from rosetta.utils import i18n as rosetta_i18n
# from .templatetags.form_error import FormErrorList
# from django.utils.translation import activate
# from .ip_utils import get_client_location

def index(request, erro=None, email_form=None, contact_form=None):

    if email_form is None:
        email_form = EmailForm(prefix='email_form')
    if contact_form is None:
        contact_form = ContactForm(prefix='contact_form')

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

from django.shortcuts import redirect
# from django.views.decorators.http import require_GET
from django.utils.translation import activate

def change_language(request):
    if request.method == 'POST':
        new_language = request.POST.get('language')
        print(f'new_language: {new_language}')
        if new_language:
            # request.session.LANGUAGE_SESSION_KEY = new_language
            print(request.session.items())
            response = activate(new_language)
            print(f'response: {response}')
    return redirect(request.META.get('HTTP_REFERER', 'pages:index'))

# @require_GET
# def switch_language(request, language_code):
    # language_code = request.GET.get('language_code')
    # translation.activate(language_code)
    # request.session['django_language'] = language_code
    # request.session[translation.LANGUAGE_SESSION_KEY] = language_code
    # Perform any additional actions if needed
    # return redirect(request.META.get('HTTP_REFERER', 'pages:index'))
    

# def switch_language(request, language_code):
#     response = set_language(request, language_code=language_code)
#     # Perform any additional actions if needed before returning the response
#     return response

def contact_form(request):
    contact_form = ContactForm(prefix='contact_form')
    template = get_template('templates/contactForm.html')
    context = {
        'title': 'Data Eden',
        'content': 'Contact Us',
        'css_url': STATIC_URL + 'pages/style.css',
        'contact_form': contact_form,
        # 'base_dir': BASE_DIR,
    }
    return HttpResponse(template.render(context, request))

def success(request, method):
    template = get_template('templates/success.html')
    context = {
        'title': 'Data Eden',
        'content': 'Success!',
        'css_url': STATIC_URL + 'pages/style.css',
        'method': method,
    }
    return HttpResponse(template.render(context))

def register_email(request): 
    # try:
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            form.save()
            print(form)
            print("Email saved successfully")
            return success(request, 'register_email')
        else:
            return index(request, erro='email', email_form=form)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # Get the form data
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Render the email template
            template = get_template('templates/email/contact.html')
            context = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            }
            message_html = template.render(context)
            message_html = mark_safe(message_html)
            connection = mail.get_connection()

            msg = " Name: " + name + "\n Subject: " + subject + "\n E-mail: " + email + "\n Message: \n\"" + message + "\""

            # Send the email
            email = mail.EmailMultiAlternatives(
                "Contato Data Eden - via Formulário de Contato",
                msg,
                django.conf.settings.EMAIL_HOST_USER,
                ['contact@dataeden.co'],
                connection=connection,
            )
            email.attach_alternative(message_html, "text/html")
            email.send()

            return success(request, 'contact')
        else:
            return index(request, erro='contact', contact_form=form)