from django.http import HttpResponse, Http404
from beauty.util.restful_resource import RESTResource
from semui.models import S, GET_staff_member
from spasui.models import M


def spa_only(f):
    def w(self, request, *args, **kw):
        print args, kw
        spa = kw.pop('spa_tag')
        # Check that the user is logged in and a spa-person, get spa.
        return f(self, request, spa, *args, **kw)
    return w


class SpaStaff(RESTResource):

    @spa_only
    def GET(self, request, spa, *args, **kw):
        pass

    @spa_only
    def PUT(self, request, spa, *args, **kw):
        pass

    @spa_only
    def POST(self, request, spa, *args, **kw):
        pass

    @spa_only
    def DELETE(self, request, spa, *args, **kw):
        pass


class SpaStaffMember(RESTResource):

    @spa_only
    def GET(self, request, spa, staff_tag, *args, **kw):
        print 'GET', spa, staff_tag
        return HttpResponse(
            GET_staff_member(spa, staff_tag),
#            S.serialize_model_to_string(M),
            content_type = 'application/rdf+xml'
        )

    @spa_only
    def PUT(self, request, spa, staff_tag, *args, **kw):
        pass

    @spa_only
    def POST(self, request, spa, staff_tag, *args, **kw):
        pass

    @spa_only
    def DELETE(self, request, spa, staff_tag, *args, **kw):
        pass
