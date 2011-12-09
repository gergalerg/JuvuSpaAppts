from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'spasui.views.spa_home', name='spa_home'),
    url(r'^iapi/', 'spasui.views.iapi', name='iapi'),
    url(r'^profile/', 'spasui.views.profile', name='profile'),
    url(r'^calendar/', 'spasui.views.calendar', name='calendar'),
    url(r'^dashboard/', 'spasui.views.dashboard', name='dashboard'),
    url(r'^dongle/', 'spasui.views.dongle', name='dongle'),
    url(r'^rad/', 'spasui.views.rad', name='rad'),
    url(r'^gnarl/', 'spasui.views.gnarl', name='gnarl'),
    )
