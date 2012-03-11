

METHODS = set('GET PUT POST DELETE'.split())


class RESTResource:

    def __call__(self, request, *args, **kw):
        if request.method in METHODS:
            m = getattr(self, request.method)
            return m(request, *args, **kw)

    def GET(self, request, *args, **kw):
        pass

    def PUT(self, request, *args, **kw):
        pass

    def POST(self, request, *args, **kw):
        pass

    def DELETE(self, request, *args, **kw):
        pass

