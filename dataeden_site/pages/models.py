from django import forms

# Create your models here.

class EmailWaitlist(forms.Form):
    email = forms.EmailField()