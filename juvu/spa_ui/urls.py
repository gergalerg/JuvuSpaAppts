from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'spa_ui.views.home', name='spa_home'),
    url(r'^cal$', 'spa_ui.views.cal', name='cal'),
    )
