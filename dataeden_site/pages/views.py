# from django.contrib.auth.models import User
import django
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.urls import reverse , resolve
from django.utils.translation import activate
from dataeden_site.settings import STATIC_URL
from .forms import EmailForm, ContactForm
from django.core import mail
from django.template.defaultfilters import mark_safe

def index(request, erro=None, email_form=None, contact_form=None):
    activate_language(request)  # Activate the appropriate language

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

def activate_language(request):
    language_code = request.GET.get('language', None)
    if language_code:
        activate(language_code)
        request.LANGUAGE_CODE = language_code
    if not language_code and 'django_language' in request.session:
        language_code = request.session['django_language']
    if not language_code:
        language_code = settings.LANGUAGE_CODE
        activate(language_code)
    print(f"activate_language: Activating language '{language_code}'")
    # request.LANGUAGE_CODE = language_code  # Set the LANGUAGE_CODE in the request object
    print(f"activate_language: request.LANGUAGE_CODE: '{request.LANGUAGE_CODE}'")

    # if language_code is None:
    #     activate_language(request)  # Activate the appropriate language
    # elif language_code:
    #     print(f"success: Activating provided language '{language_code}'")
    #     activate(language_code)  # Activate the provided language
    # elif 'django_language' in request.session:
    #     session_language_code = request.session['django_language']
    #     print(f"success: Activating session language '{session_language_code}'")
    #     activate(session_language_code)  # Activate the session language
    # else:
    #     default_language_code = settings.LANGUAGE_CODE
    #     print(f"success: Activating default language '{default_language_code}'")
    #     activate(default_language_code)  # Activate the system language


def success(request, method, language_code=None):

    activate_language(request)  # Activate the appropriate language

    context = {
        'title': 'Data Eden',
        'content': 'Success!',
        'css_url': STATIC_URL + 'pages/style.css',
        'method': method,
        # 'full_url': request.build_absolute_uri(),
    }
    # template_name = 'templates/success.html'  # Replace with the actual template path
    # Render the success template with the context
    template_name = 'templates/success.html'
    return render(request, template_name, context)


def change_language(request):
    new_language = request.GET.get('language')
    # print(f'new_language: {new_language}')

    lower_languages = {key.lower(): value for key, value in settings.LANGUAGES}
    new_language_lower = new_language.lower()
    
    if new_language_lower in lower_languages:
        # print('Entrou no if do change_language')

        request.session['django_language'] = new_language
        request.session['rosetta_i18n_language'] = new_language

        response = HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('pages:index')))

        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, new_language)
        referer_language_code = '/' + request.LANGUAGE_CODE + '/'
        new_language_code = '/' + new_language + '/'
        response['Location'] = response['Location'].replace(referer_language_code, new_language_code)
        return response
    print('CHEGOU AQIO')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('pages:index')))

#   change_language POST

# def change_language(request):
#     if request.method == 'POST':
#         new_language = request.POST.get('language')
#         # print(f'new_language: {new_language}')
#         if new_language:
#             response = HttpResponse()  # Create an HttpResponse object
#             response = redirect(request.META.get('HTTP_REFERER', 'pages:index'))
#             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, new_language)
#             response['Location'] = response['Location'].replace(f'/{request.LANGUAGE_CODE}/', f'/{new_language}/')
#             print(f'response: {response}')
#             return response
#     return redirect(request.META.get('HTTP_REFERER', 'pages:index'))

#   change_language GET


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

# def contact_form(request):
#     contact_form = ContactForm(prefix='contact_form')
#     template = get_template('templates/contactForm.html')
#     context = {
#         'title': 'Data Eden',
#         'content': 'Contact Us',
#         'css_url': STATIC_URL + 'pages/style.css',
#         'contact_form': contact_form,
#         # 'base_dir': BASE_DIR,
#     }
#     return HttpResponse(template.render(context, request))



def register_email(request): 
    activate_language(request)  # Activate the appropriate language
    print(request.LANGUAGE_CODE)
    # try:
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            form.save()
            print(form)
            print("Email saved successfully")
            return redirect('pages:success', method='register_email')
            # return success(request, method='register_email')
            # return success(request, method='register_email', language_code=request.LANGUAGE_CODE)

            # return success(request, 'register_email')
        else:
            return index(request, erro='email', email_form=form)

def contact(request):
    activate_language(request)  # Activate the appropriate language
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

            return redirect('pages:success', method='contact')
            # return success(request, 'contact', language_code=request.LANGUAGE_CODE)
        else:
            return index(request, erro='contact', contact_form=form)
    else:
        if request.GET:
            # If there is GET data, initialize the form with it
            form = ContactForm(request.GET)
        else:
            # Create an instance of the ContactForm and pass it to the template
            form = ContactForm(request.POST)
        return render(request, 'templates/index.html', {'contact_form': form})       
