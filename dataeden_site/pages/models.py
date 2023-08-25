# from django import forms
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
# from .views import index
# from .forms import EmailForm, ContactForm
from django.core.exceptions import ObjectDoesNotExist
from django.core import mail
from django.template.defaultfilters import mark_safe
from django.utils.translation import activate
from django.urls import reverse
from django.template.loader import get_template

# from django.conf import HOST_EMAIL_USER
from django.conf import settings

# Create your models here.

class LanguageManager(models.Manager):
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

    def change_language(request):
        new_language = request.GET.get('language')

        lower_languages = {key.lower(): value for key, value in settings.LANGUAGES}
        new_language_lower = new_language.lower()
        
        if new_language_lower in lower_languages:

            request.session['django_language'] = new_language
            request.session['rosetta_i18n_language'] = new_language

            response = HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('pages:index')))

            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, new_language)
            referer_language_code = '/' + request.LANGUAGE_CODE + '/'
            new_language_code = '/' + new_language + '/'
            response['Location'] = response['Location'].replace(referer_language_code, new_language_code)
            return response
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('pages:index')))


class EmailAddress(models.Model):     
    email = models.EmailField(unique=True)

    @staticmethod
    def save_email(form):

        if form.is_valid():
            email = form.cleaned_data.get('email')
            
            try:
                # Check if the email already exists in the database
                existing_email = EmailAddress.objects.get(email=email)
                print("Email already exists:", email)
                # Handle the duplicate email case
                return HttpResponse("Email already registered", status=400)
            
            except ObjectDoesNotExist:
                # Email doesn't exist, proceed with saving
                form.save()
                print("Email saved successfully")
                return redirect('pages:success', method='register_email')
        else:
            return HttpResponse("Invalid email", status=400)

    class Meta:
        verbose_name = "Email Address"
        verbose_name_plural = "Email Addresses"

    app_label = 'pages'
class ContactModel(models.Model):     
    name = models.CharField()
    email = models.EmailField()
    subject = models.CharField()
    message = models.CharField()

    @staticmethod
    def contact(request, form):
        if request.method == 'POST':

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
                    settings.EMAIL_HOST_USER,
                    ['contact@dataeden.co'],
                    connection=connection,
                )
                email.attach_alternative(message_html, "text/html")
                email.send()

                return redirect('pages:success', method='contact')
                # return success(request, 'contact', language_code=request.LANGUAGE_CODE)
            else:
                # return index(request, erro='contact', contact_form=form)
                return HttpResponseRedirect('pages:index?erro=contact')
        else:
            return render(request, 'templates/index.html', {'contact_form': form})   

    app_label = 'pages'