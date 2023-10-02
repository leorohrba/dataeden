from django.contrib import admin
from .models import EmailAddress, ContactModel, Lead

# Register your models here.

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject',)

class EmailModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'decrypted_email', 'email',)

admin.site.register(EmailAddress, EmailModelAdmin)
admin.site.register(ContactModel, ContactModelAdmin)
admin.site.register(Lead)

