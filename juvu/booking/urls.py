from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'booking.views.home', name='booking_home'),
    url(r'^inv$', 'booking.views.inv', name='inv'),
    url(r'^book$', 'booking.views.book', name='book'),
    url(r'^bid$', 'splash.views.bid', name='bid'),
    )
