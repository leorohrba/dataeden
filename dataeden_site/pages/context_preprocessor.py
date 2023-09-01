from django.conf import settings

def languages(request):
    return {
        # 'LANGUAGES': settings.LANGUAGES,
        'LANGUAGE_MAP': settings.LANGUAGE_MAP,
        # 'LANGUAGE_CODE': settings.LANGUAGE_CODE,
        # 'language_country_mapping': settings.LANGUAGE_COUNTRY,
    }
