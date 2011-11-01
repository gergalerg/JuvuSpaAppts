from repui.search import ensure_fields, dates, DATE_FORMAT
from repui.models import (
    add_treatment_to_trenche,
    create_availability_with_trenche,
    subject,
    )


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

        res = P(s, o, args)

        if __debug__:
            print s, '->', p, '->', o, '. COMPLETED'

        return res

    @_mark_api_method
    def add_treatment_to_trenche(self, s, o, args):
        add_treatment_to_trenche(s, o)
        return True

    @_mark_api_method
    def create_availability_with_trenche(self, s, o, args):
        days = dates(**ensure_fields(args))
        for day in days:
            day = day.strftime(DATE_FORMAT)
            create_availability_with_trenche(s, day)
        return True

    @_mark_api_method
    def subject(self, s, o, args):
        return subject()


dispatch = Dispatch()
