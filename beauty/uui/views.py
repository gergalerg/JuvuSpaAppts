from pprint import pprint as _P
from json import dumps
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
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

    results, criteria = _get_results(request)

    s = YelpApi(criteria['treatment'], criteria['location'], '5')

    return render_to_response(
        'results.html',
        dict(
            what = criteria['treatment_full_text'],
            where = criteria['location_full_text'],
            deal_calendar = DealCalendar(criteria['this_day_date']).get_table(),
            lat_long = criteria['lat_long'],
            next_day = criteria['next_day'],
            this_day = criteria['this_day'],
            ),
        context_instance=RequestContext(request),
        )


def ajax_results(request):
    assert request.method == 'POST'
    results, _ = _get_results(request)
    return HttpResponse(results, mimetype="application/json")


def _get_results(request):
    if __debug__:
        _P(request.POST)
    criteria = process_POST_params(request)
    if __debug__:
        print 'post process_POST_params() ->'
        _P(criteria)
        print
    results = dumps(search_for_availabilities(**criteria))
    return results, criteria


def booking(request):
    return render_to_response(
        'booking.html',
        )


def confirmation(request):
    return render_to_response(
        'confirmation.html',
        )

