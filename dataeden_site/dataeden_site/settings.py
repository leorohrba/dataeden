"""
Django settings for dataeden_site project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b9xk&q#0o9^so2zjb&mqhhc4pnqnhqt5tu*5t&ic401kue%#7)'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('pt-BR', _('Portuguese')),
]

LANGUAGE_MAP = {
    'en': 'us',  # Example: 'US' country code maps to English language
    'pt-BR': 'br',  # Example: 'BR' country code maps to Portuguese language
    # Add more country code to language mappings as needed
}

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_media/')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'staticfiles'),
#     # os.path.join(BASE_DIR, 'admin'),
# ]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static').replace("\\", "/"),
    # os.path.join(BASE_DIR, 'staticfiles').replace("\\", "/"),
]
COMPRESS_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#DEVELOPMENT
STATICFILES_STORAGE = 'dataeden_site.storage.FileSystemStorage'
#PRODUCTION
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_CONTENT_TYPES = [
    ('text/css', 'css'),
    ('application/javascript', 'js'),
    ('image/png', 'png'),
]

TEMPLATE_CONTEXT_PROCESSORS = 'django.core.context_processors.static'

STATICFILES_FINDERS = [
    'compressor.finders.CompressorFinder',
]

TEMPLATE_FILTERS = {
    'as_divs': 'my_app.templatetags.as_divs',
}

internal_ips = ['127.0.0.1', ]
if DEBUG:    
    import socket
    hostname, _, ips =socket.gethostbyname_ex(socket.gethostname())
    internal_ips += [ip[:-1] + '1' for ip in ips]
    import mimetypes
    mimetypes.add_type("image/png", ".png", True)
    mimetypes.add_type("text/html", ".html", True)
    mimetypes.add_type("text/css", ".css", True)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG,
    'DEBUG_TOOLBAR_CLASS': 'pages.debug_toolbar.CustomDebugToolbar',
}


INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'compressor',
    'django.contrib.staticfiles',
    'rosetta',
    'ipware',
    'debug_toolbar',
]

COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = [
    ('text/x-scss','django_libsass.SassCompiler'),
]

DEFAULT_FROM_EMAIL = "contact@dataeden.co"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

# APPEND_SLASH = False

# Map country codes to languages

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
] 


SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

ROOT_URLCONF = 'dataeden_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR,
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'admin'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_preprocessor.languages',
            ],
            "libraries": {
                "form_error": "pages.templatetags.form_error",
                "admin.urls": "django.contrib.admin.templatetags.admin_urls",
            },
        },
    },
]

WSGI_APPLICATION = 'dataeden_site.wsgi.application'

ALLOWED_HOSTS = ['localhost', 'db', '127.0.0.0', '127.0.0.1', '172.18.0.2', '172.18.0.3', '0.0.0.0']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'dataeden',
        # 'USER': os.environ.get('POSTGRES_USER'),
        # "HOST": "11.23.34.2",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
        "HOST": "db",  # set dynamically
        # "HOST": "",  # QUANDO MIGRATE
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'noreply.dataeden@gmail.com'
EMAIL_HOST_PASSWORD = 'afszkknjzrjnxsgg'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/


# LANGUAGE_COUNTRY = {
#     'en': 'us',
#     'pt-BR': 'br',
#     # Add more mappings as needed
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
