from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'splash.views.splash', name='splash'),
    url(r'^thanks$', 'splash.views.thanks', name='thanks'),
    url(r'^uh$', 'splash.views.record_email', name='record_email'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # User-facing site.
    url(r'^look/', include('look.urls')),

    )

# Static media (served directly by the web server in production.)
if not settings.PRODUCTION:
    urlpatterns += patterns('',
        (
            r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT},
            ),
        )
