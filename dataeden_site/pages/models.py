# from django import forms
from django.db import models

# Create your models here.
class EmailAddress(models.Model):     
    email = models.EmailField()

    class Meta:
        verbose_name = "Email Address"
        verbose_name_plural = "Email Addresses"

    app_label = 'pages'
class ContactModel(models.Model):     
    name = models.CharField()
    email = models.EmailField()
    subject = models.CharField()
    message = models.CharField()

    app_label = 'pages'