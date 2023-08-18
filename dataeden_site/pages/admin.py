from django.contrib import admin
from .models import EmailAddress, ContactModel

# Register your models here.

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject',)

class EmailModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)

admin.site.register(EmailAddress, EmailModelAdmin)
admin.site.register(ContactModel, ContactModelAdmin)
