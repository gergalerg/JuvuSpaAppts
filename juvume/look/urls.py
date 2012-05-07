from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'look.views.home', name='booking_home'),
    )
