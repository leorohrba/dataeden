from django.urls import path
# from django.views.i18n import set_language
from .views import index, register_email, success, contact, change_language
# , about_us, base

app_name = "pages"
urlpatterns = [
    path("", index, name="index"),
    # path('set_language/<str:language_code>/', change_language, name='set_language'),
    path('set_language/', change_language, name='set_language'),
    # path('set_language/',  set_language(), name='set_language'),
    path("index/", index, name="index"),
    path("contact/", contact, name="contact"),
    path("email/", register_email, name='registerEmail'),
    path('success/<str:method>/', success, name='success'),
    # path('<str:language_code>/success/<str:method>/', success, name='success'),
    # path("success/", success, name='success'),
]

# Replace 'YOUR_API_KEY' with your actual ipstack API key
# api_key = '8481f3f20543580be67d3bce342fa7ff'
# ip_address = '8.8.8.8'  # Example IP address
# country_code = get_country_code_from_ip(ip_address, api_key)
# print(f"Country code for {ip_address}: {country_code}")