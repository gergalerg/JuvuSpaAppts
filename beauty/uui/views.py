from pprint import pprint as _P
from json import dumps
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from spasui.search import process_POST_params, search_for_availabilities
from beauty.util.dealcal import DealCalendar
from yelp import YelpApi


def search(request):
    '''
    Search page.
    '''
    return render_to_response(
        'search.html',
        context_instance=RequestContext(request),
        )


def results(request):
    if request.method != 'POST':
        return redirect('search')

    if __debug__:
        _P(request.POST)

    criteria = process_POST_params(request)
    if __debug__:
        print 'post process_POST_params() ->'
        _P(criteria)
        print

    s = YelpApi(criteria['treatment'], criteria['location'], '5')

    return render_to_response(
        'results.html',
        {'spas': s.results, 'total': s.total, 'criteria': criteria},
        context_instance=RequestContext(request),
        )

def booking(request):
    return render_to_response(
        'booking.html',
        )


def confirmation(request):
    return render_to_response(
        'confirmation.html',
        )

