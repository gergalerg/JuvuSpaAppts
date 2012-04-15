from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'spa_ui.views.home', name='spa_home'),
    url(r'^cal$', 'spa_ui.views.cal', name='cal'),
    url(r'^merchant$', 'spa_ui.views.merchant', name='merchant'),
    url(
        r'^merchant_reviews$',
        'spa_ui.views.merchant_reviews',
        name='merchant_reviews',
        ),
    url(
        r'^merchant_services$',
        'spa_ui.views.merchant_services',
        name='merchant_services',
        ),
    )
