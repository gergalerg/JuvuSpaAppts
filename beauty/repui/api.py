

_API_METHODS = set()


def _mark_api_method(func):
    _API_METHODS.add(func.__name__)
    return func


class Dispatch:

    def __call__(self, s, p, o, **args):
        s, p, o = s[0], p[0], o[0]
        if __debug__:
            print s, p, o, args
        if p not in _API_METHODS:
            if __debug__:
                print 'unknown API call:', p
            return False
        p = getattr(self, p)
        return p(s, o)

    @_mark_api_method
    def drop_treatment_from_trenche(self, s, o):
        if __debug__:
            print 'drop_treatment_from_trenche', s, '->', o
        return True


dispatch = Dispatch()
