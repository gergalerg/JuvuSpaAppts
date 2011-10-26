from repui.models import add_treatment_to_trenche


_API_METHODS = set()


def _mark_api_method(func):
    _API_METHODS.add(func.__name__)
    return func


class Dispatch:

    def __call__(self, s, p, o, **args):
        s, p, o = [str(term[0]) for term in (s, p, o)]
        if __debug__:
            print s, p, o, args

        if p not in _API_METHODS:
            if __debug__:
                print 'unknown API call:', p
            return False

        P = getattr(self, p)

        if __debug__:
            print s, '->', p, '->', o

        res = P(s, o)

        if __debug__:
            print s, '->', p, '->', o, '. COMPLETED'

        return res

    @_mark_api_method
    def add_treatment_to_trenche(self, s, o):
        add_treatment_to_trenche(s, o)
        return True


dispatch = Dispatch()
