from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'splash.views.splash', name='splash'),
    url(r'^thanks$', 'splash.views.thanks', name='thanks'),
    url(r'^uh$', 'splash.views.record_email', name='record_email'),
    url(r'^login/$', 'accounts.views.login', name='login'),
    url(r'^calendar$', 'splash.views.calendar', name='calendar'),
    url(r'^inv$', 'splash.views.inv', name='inv'),
    url(r'^book$', 'splash.views.book', name='book'),
    url(r'^bid$', 'splash.views.bid', name='bid'),
    url(r'^merchant$', 'splash.views.merchant', name='merchant'),
    url(r'^merchant_reviews$', 'splash.views.merchant_reviews', name='merchant'),
    url(r'^merchant_services$', 'splash.views.merchant_services', name='merchant'),
    url(r'^book_info$', 'splash.views.book_info', name='book_info'),
    url(r'^book_confirm$', 'splash.views.book_confirm', name='book_confirm'),
    url(r'^book_congrats$', 'splash.views.book_congrats', name='book_congrats'),
    url(r'^bid_info$', 'splash.views.bid_info', name='bid_info'),
    url(r'^bid_confirm$', 'splash.views.bid_confirm', name='bid_confirm'),

	
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
