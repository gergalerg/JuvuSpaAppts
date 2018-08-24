from django.conf.urls.defaults import patterns, url
from semui.views import SpaStaff, SpaStaffMember

urlpatterns = patterns('',
#    url(r'^$', 'semui.views.', name=''),

#    url(r'^spa/(?P<spa_tag>[a-zA-Z_]+)$', 'semui.views.', name=''),
    url(r'^spa/(?P<spa_tag>[a-zA-Z_]+)/staff/?$', SpaStaff(), name='staff'),
    url(
        r'^spa/(?P<spa_tag>[a-zA-Z_]+)/staff/(?P<staff_tag>[a-zA-Z_]+)$',
        SpaStaffMember(),
        name='staff_member',
        ),
    )
