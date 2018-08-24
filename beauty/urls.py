from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()


urlpatterns = patterns('',

    # Django Admin (unused so far.)
    (r'^admin/', include(admin.site.urls)),

    url(r'^signup/?', 'uui.views.signup', name='signup'),

    # User-facing site, 'uui' app.
    url(r'^$', 'uui.views.search', name='search'),
    url(r'^results/', 'uui.views.results', name='results'),
    url(r'^res/', 'uui.views.ajax_results', name='ares'),
    url(r'^booking/', 'uui.views.booking', name='booking'),
    url(r'^confirmation/', 'uui.views.confirmation', name='confirmation'),
    url(r'^logout/',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name='logout'),

    url(r'^login/',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name='login'),

    # Spa-facing site.
    url(r'^spa/', include('spasui.urls')),

    # Rep's support site, apps.
    url(r'^repui/?$', 'repui.views.index', name='repui'),

    # Semantic REST API.
    url(r'^ref/', include('semui.urls')),

    # Static media (should be served directly by the web server in production.)
    (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT},
        ),

    )
