from pprint import pprint as _P
from json import dumps
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from spasui.search import process_POST_params, search_for_availabilities
from beauty.util.dealcal import DealCalendar
from yelp import YelpApi
from spasui.forms import SpaInfoForm
from beauty.uui.forms import UserSignupForm
from beauty.data.treatments import TREEd
from simplejson import dumps


def search(request):
    '''
    Search page.
    '''
    if request.user.is_authenticated():
        name = request.user.first_name
    else:
        name = 'Me'
    tree = TREEd.copy()
    tree['name'] = name
    return render_to_response(
        'search_home.html',
        dict(
            name=name,
            form=SpaInfoForm(),
            tree_data=dumps(tree),
            ),
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


def signup(request):
    if request.method != 'POST':
        form = UserSignupForm()
    else:
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['email'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
                )
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                )
            login(request, user)
            return HttpResponseRedirect('/#step/0')
        else:
            pass

    return render_to_response(
        'signup.html',
        dict(form=form),
        context_instance=RequestContext(request),
        )


def booking(request):
    return render_to_response(
        'booking.html',
        )


def confirmation(request):
    return render_to_response(
        'visibits.html',
        )

