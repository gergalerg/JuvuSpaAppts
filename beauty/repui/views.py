from collections import defaultdict
from json import dumps
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from repui.api import dispatch
from repui.models import get_trenche_support
from repui.search import process_POST_params, search_for_availabilities
from beauty.data.treatments import TREATMENTS
from beauty.util.dealcal import DealCalendar

#=---- - - - - - - - - - - - - - - - - - - - - - - - -
#
# API service.


def _json_boolean(n):
    return ("false", "true")[bool(n)]


def iapi(request):
    if __debug__:
        print request.POST
    res = dispatch(**request.POST)
    return HttpResponse(
        _json_boolean(res),
        mimetype="application/json",
        )


#=---- - - - - - - - - - - - - - - - - - - - - - - - -
#
# Main page of the iPad reps' UI.


def _prepare_trenche_data():
    d = defaultdict(list)
    for r in get_trenche_support():
        d[str(r['trenchelabel'])].append(str(r['treatmentname']))
    for default_trenche in "ABC":
        if default_trenche not in d:
            d[default_trenche] # force appearance of key.
    return [
        (k, sorted(d[k]))
        for k in sorted(d)
        ]


_t = [(k, TREATMENTS[k]) for k in sorted(TREATMENTS)]


def index(request):
    '''
    Rep UI page.
    '''
    return render_to_response(
        'index.html',
        dict(
            treatments=_t,
            trenches=_prepare_trenche_data(),
            ),
        context_instance=RequestContext(request),
        )


#=---- - - - - - - - - - - - - - - - - - - - - - - - -
#
# Search for available appointments.

from pprint import pprint as _P


def home(request):
    '''
    Search page.
    '''

    return render_to_response(
        'search.html',
        dict(),
        context_instance=RequestContext(request),
        )

def profile(request):
    return render_to_response(
        'profile.html',
        )

def search(request):
    if request.method != 'POST':
        return redirect('home')

    if __debug__:
        _P(request.POST)

    criteria = process_POST_params(request)
    if __debug__:
        print 'post process_POST_params() ->'
        _P(criteria)
        print

    return render_to_response(
        'results.html',
        dict(
            results = dumps(search_for_availabilities(**criteria)),
            what = criteria['treatment_full_text'],
            where = criteria['location_full_text'],
            deal_calendar = DealCalendar().get_table(),
            lat_long = criteria['lat_long'],
            ),
        context_instance=RequestContext(request),
        )


##    <QueryDict: {
##        u'csrfmiddlewaretoken': [u'db4187ab0c4fe8ef8859b2e9948ecaba'],
##        u'location': [u'San Francisco'],
##        u'treatment': [u'massage'],
##        u'today': [u'on'],
##        u'anotherday': [u'']
##        }>






















