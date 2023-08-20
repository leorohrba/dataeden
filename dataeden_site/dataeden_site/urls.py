"""
URL configuration for dataeden_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns
# from pages.views import switch_language
# from django.views.i18n import set_language
# from pages.views import index

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('static/', include('django.contrib.staticfiles.urls')),
    # path("i18n/", include("django.conf.urls.i18n")),
] 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += i18n_patterns(
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('', include('pages.urls', namespace='pages')),
)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += i18n_patterns(
    # re_path(r'^(?P<language_code>[-\w]+)/i18n/setlang/$', set_language, name='set_language'),
    # re_path(r'^(?P<language_code>[-\w]+)/$', set_language, name='set_language'),
    
    # adicionar codigo da lingua na url
    # path('i18n/', include('django.conf.urls.i18n')),
    # path('', include('pages.urls', namespace='pages')),
    # path('<str:language_code>/', include('pages.urls')),
    
    # path('static/', include('django.contrib.staticfiles.urls')),
# )
