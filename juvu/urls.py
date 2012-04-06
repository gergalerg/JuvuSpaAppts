from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'splash.views.splash', name='splash'),
    url(r'^thanks$', 'splash.views.thanks', name='thanks'),
    url(r'^uh$', 'splash.views.record_email', name='record_email'),
    url(r'^login$', 'accounts.views.login', name='login'),
    url(r'^inv$', 'splash.views.inv', name='inv'),
    url(r'^book$', 'splash.views.book', name='book'),
    url(r'^bid$', 'splash.views.bid', name='bid'),
    url(r'^merchant$', 'splash.views.merchant', name='merchant'),

    # User-facing site.
    url(r'^look/', include('booking.urls')),

    # Spa-facing site.
    url(r'^spa/', include('spa_ui.urls')),

    # Internal introspection site.
    url(r'^innerview/', include('innerview.urls')),

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
