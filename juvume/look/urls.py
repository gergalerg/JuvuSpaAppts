from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'look.views.home', name='booking_home'),
    url(r'^inv$', 'look.views.inv', name='inv'),
    url(r'^book$', 'look.views.book', name='book'),
    url(r'^book_info$', 'look.views.book_info', name='book_info'),
    url(r'^book_confirm$', 'look.views.book_confirm', name='book_confirm'),
    url(r'^book_congrats$', 'look.views.book_congrats', name='book_congrats'),
    url(r'^hooray$', 'look.views.hooray', name = 'hooray'),
    )
