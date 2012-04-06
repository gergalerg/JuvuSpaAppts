from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'innerview.views.home', name='innerview_home'),
    )
