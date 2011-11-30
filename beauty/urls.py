from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()


urlpatterns = patterns('',

    # Django Admin (unused so far.)
    (r'^admin/', include(admin.site.urls)),

    # User-facing site, 'uui' app.
    url(r'^$', 'uui.views.search', name='search'),
    url(r'^results/', 'uui.views.results', name='results'),
    url(r'^booking/', 'uui.views.booking', name='booking'),
    url(r'^confirmation/', 'uui.views.confirmation', name='confirmation'),

    # Spa-facing site.
    url(r'^iapi/', 'spasui.views.iapi', name='iapi'),
    url(r'^profile/', 'spasui.views.profile', name='profile'),
    url(r'^calendar/', 'spasui.views.calendar', name='calendar'),
    url(r'^dashboard/', 'spasui.views.dashboard', name='dashboard'),
    url(r'^info/', 'spasui.views.info', name='info'),
    url(r'^dongle/', 'spasui.views.dongle', name='dongle'),

    # Rep's support site, apps.
    url(r'^repui/?$', 'repui.views.index', name='repui'),

    # Static media (should be served directly by the web server in production.)
    (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT},
        ),

    )
