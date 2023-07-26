from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
import os

from dataeden_site.settings import STATIC_URL, BASE_DIR
from .models import EmailWaitlist

# path = os.path.join(os.path.dirname(__file__), 'html/')

def index(request):
    template = loader.get_template('templates/index.html')
    context = {
        'title': 'Data Eden',
        'content': 'Welcome to Data Eden',
        'css_url': STATIC_URL + 'pages/style.css',
        # 'base_dir': BASE_DIR,
    }
    return HttpResponse(template.render(context, request))

def register_email(request):
    form = EmailWaitlist(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")

        