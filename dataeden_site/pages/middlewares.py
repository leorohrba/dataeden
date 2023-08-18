
from django.conf import settings
from .ip_utils import get_client_location
# from django.utils import translation
from django.urls import resolve
from django.utils.translation import activate, get_language
from django.http import HttpResponseRedirect
# from django.settings import LANGUAGE_MAP

# class GetUserLocationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         language_code = resolve(request.path_info).kwargs.get('language_code')
#         print(f'catch language_code: {language_code}')
#         if hasattr(request, 'resolver_match') and request.resolver_match is not None:
#             print('entrou no 1 if')
#             if request.resolver_match.url_name == 'set_language':
#                 print('entrou no 2 if')
#                 language_switch = True
#                 language = language_code
#                 print(f'language_switch dentro dos dois ifs: {language_switch}')
#         else:
#             language_switch = False
#             print(f'language_switch dentro do else: {language_switch}')


#         if not language_switch:
#             # if not request.session.get('django_language'):
#             country_code = get_client_location(request)
#             language = settings.LANGUAGE_MAP.get(country_code, 'en')  # Default to 'en'

#             print(f'language: {language}')

#         request.session['django_language'] = language
#         response = self.get_response(request)
#         return response

# from django.shortcuts import redirect


# class LanguageMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         language_code = resolve(request.path_info).kwargs.get('language_code')

#         print(f'language_code: {language_code}')

#         # Check if the current view is the language switch view
#         is_language_switch = request.resolver_match.url_name == 'set_language'

#         if is_language_switch:
#             # Redirect to the appropriate URL without changing the language
#             return redirect(reverse('pages:index'))

#         if language_code:
#             activate(language_code)
#             request.LANGUAGE_CODE = get_language()

#         response = self.get_response(request)
#         return response

#     def __call__(self, request):
#         # Check if language is set in the URL parameter
#         language_code = resolve(request.path_info).kwargs.get('language_code')

#         if language_code:
#             activate(language_code)
#             request.LANGUAGE_CODE = get_language()

#         response = self.get_response(request)
#         print(response)
#         return response

# class LanguagePrefixMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Get the language code from the URL
#         language_code = request.path_info.strip('/').split('/')[0]
        
#         # Check if the language code is valid
#         valid_language_codes = [lang[0] for lang in settings.LANGUAGES]
#         if language_code in valid_language_codes:
#             # Set the language for this request
#             activate(language_code)

#             # Process the view for this request
#             response = self.get_response(request)

#             # Redirect to the same URL with the language prefix
#             redirect_url = f'/{language_code}{request.path_info}'
#             if request.GET:
#                 redirect_url += f'?{request.GET.urlencode()}'
#             return HttpResponseRedirect(redirect_url)
    
#     # If the language code is not valid, continue processing
#         return self.get_response(request)