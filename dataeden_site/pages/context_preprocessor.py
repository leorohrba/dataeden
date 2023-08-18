from django.conf import settings

def languages(request):
    return {
        'LANGUAGES': settings.LANGUAGES,
        'LANGUAGE_MAP': settings.LANGUAGE_MAP,
        # 'language_country_mapping': settings.LANGUAGE_COUNTRY,
    }
