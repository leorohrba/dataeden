# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
from pages.models import EmailAddress, ContactModel
from django import forms
from django.core.validators import EmailValidator
from .templatetags.form_error import FormErrorList

class EmailForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, required=True)
    error_class = FormErrorList

    # def __str__(self):
    #     return self._meta.db_table
    
    def __init__(self, *args, **kwargs):
        kwargs.update({'error_class': FormErrorList})
        super().__init__(*args, **kwargs)
        # self.fields['email'].validators.append(EmailValidator())
        # self.fields['email'].widget.attrs['placeholder'] = 'Email'

    class Meta:
        model = EmailAddress
        fields = ['email']
        # error_class = FormErrorList

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField()
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)
    
    error_class = FormErrorList
    
    class Meta:
        model = ContactModel
        fields = ['name',
                  'email',
                  'subject',
                  'message']
        # error_class = FormErrorList
    
    def __init__(self, *args, **kwargs):
        kwargs.update({'error_class': FormErrorList})
        super().__init__(*args, **kwargs)
    
    # def __str__(self):
    #     return self.email


