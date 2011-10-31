from collections import defaultdict
from datetime import date, timedelta, datetime
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from repui.models import get_trenche_support
from beauty.data.treatments import TREATMENTS, lookup_treatment


DATE_FORMAT = '%m/%d/%Y'
EXPECTED_FIELDS = [
    'location',
    'treatment',
    'today',
    'tomorrow',
    'thenextday',
    'anotherday',
    ]


def process_POST_params(request):
    data = dict(
        (name, request.POST.get(name))
        for name in EXPECTED_FIELDS
        )

    if __debug__:
        print data

    data['lat_long'], data['distance_full_text'] = _distance(**data)
    data['dates'] = dates(**data)
    treatment = data['treatment']
    data['treatment_full_text'] = lookup_treatment(treatment) or treatment
    return data


def dates(today, tomorrow, thenextday, anotherday, **_):
    '''
    Create a list of datetime.date objects for each of the selected days.

    TODO anotherday should be converted by form validation.
    '''
    days, t, d = [], date.today(), timedelta(days=1)
    if today:
        days.append(t)
    t += d
    if tomorrow:
        days.append(t)
    t += d
    if thenextday:
        days.append(t)
    if anotherday:
        t = datetime.strptime(anotherday, DATE_FORMAT).date()
        days.append(t)
    return days


def _distance(location, **_):
    '''
    Do some sort of geo-lookup and figure out a (latitude, longitude)
    pair and a "canonical" display string for the address (or whatever
    was entered.)

    Should possibly raise one of these (unimplemented) exceptions:
        AmbiguousLocationError (too many results)
        NoLocationError (zero results)
        ServiceInterruption (something went wrong, but it's not due to
            user's search.)
    '''
    return (1, 2), "Where I Left My Heart, CA 94132"


##
##    <QueryDict: {
##        u'csrfmiddlewaretoken': [u'db4187ab0c4fe8ef8859b2e9948ecaba'],
##        u'location': [u'San Francisco'],
##        u'treatment': [u'massage'],
##        u'today': [u'on'],
##        u'anotherday': [u'']
##        }>
##





















