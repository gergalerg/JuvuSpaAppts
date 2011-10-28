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
    )

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'repui.views.index', name='home'),
    (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT},
        ),
    url(r'^iapi/', 'repui.views.iapi', name='iapi'),
    url(r'^search/', 'repui.views.search', name='search'),
    (
        r'^dyn/search.css$',
        direct_to_template,
        dict(
            template='search.css',
            extra_context=dict(
                colors=COLORS,
                ),
            mimetype='text/css',
            ),
        ),
    )
