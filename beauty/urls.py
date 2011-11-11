from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

COLORS = dict(
    bg='#eeffee',

    header='#003300',
    header_bg='#fff',

    main='#003300',
    main_bg='#dfd',

    results='#003300',
    results_bg='#fff',

    tools='#003300',
    tools_bg='#fff',

    )

urlpatterns = patterns('',

    # Django Admin (unused so far.)
    (r'^admin/', include(admin.site.urls)),

    # User-facing site, 'uui' app.
    url(r'^$', 'uui.views.home', name='home'),
    ( # Actually, this is the CSS for 'home'.
        r'^dyn/search.css$',
        direct_to_template,
        dict(
            template='search.css',
            extra_context=dict(colors=COLORS),
            mimetype='text/css',
            ),
        ),

    (
        r'^dyn/results.css$',
        direct_to_template,
        dict(
            template='results.css',
            extra_context=dict(colors=COLORS),
            mimetype='text/css',
            ),
        ),

    url(r'^search/', 'uui.views.search', name='search'),
    url(r'^booking/', 'uui.views.booking', name='booking'),
    url(r'^confirmation/', 'uui.views.confirmation', name='confirmation'),

    # Spa-facing site.
    url(r'^iapi/', 'spasui.views.iapi', name='iapi'),
    url(r'^profile/', 'spasui.views.profile', name='profile'),
    url(r'^calendar/', 'spasui.views.calendar', name='calendar'),

    # Rep's support site, apps.
    url(r'^repui/?$', 'repui.views.index', name='repui'),

    # Static media (should be served directly by the web server in production.)
    (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT},
        ),

    ),
)
