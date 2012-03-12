# API service.
from datetime import datetime
from pprint import pprint as _P
from itertools import groupby
from json import dumps
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from spasui.models import prepare_trenche_data
from spasui.api import dispatch
from spasui.availabilities import create_availabilities
from spasui.forms import SpaInfoForm
from beauty.data.treatments import TREE


def _json_boolean(n):
    return ("false", "true")[bool(n)]


STAFF = [
    {'name': 'Billy'},
    {'name': 'Bob'},
    {'name': 'Billy Jo Bob'},
    ]


def spa_home(request):
    return render_to_response(
        'spa_home.html',
        dict(
#            spa_name='Sports Club LA',
            form=SpaInfoForm(),
            tree_data=TREE,
            staff=STAFF,
            ),
        context_instance=RequestContext(request),
        )


def iapi(request):
    if __debug__:
        print request.POST
    res = dispatch(**request.POST)
    return HttpResponse(
        _json_boolean(res),
        mimetype="application/json",
        )


def profile(request):
    return render_to_response('profile.html')


def calendar(request):
    if request.method == 'POST':
        return post_calendar(request)

    return render_to_response(
        'calendar.html',
        dict(
            locations=[
                dict(
                    label='loc_sox%i' % n,
                    name="%i Barny's" % n,
                    )
                for n in range(8)
                ],
            trenches=prepare_trenche_data(),
            ),
        context_instance=RequestContext(request),
        )


def post_calendar(request):
    print 'HI!'
    return render_to_response(
        'calendar.html',
        dict(
            locations = [
                dict(
                    label='loc_sox%i' % n,
                    name="%i Barny's" % n,
                    )
                for n in range(8)
                ],
            trenches = prepare_trenche_data(),
            results = list(create_availabilities(request.POST)),
            ),
        context_instance=RequestContext(request),
        )


def dashboard(request):
    return render_to_response(
        'dashboard.html',
        dict(tree_data=TREE),
        context_instance=RequestContext(request),
        )


def info(request):

    if request.method == 'POST':
        form = SpaInfoForm(request.POST)
        if form.is_valid():
            process_form(**form.cleaned_data)
            return HttpResponse("Form submitted")
    else:
        form = SpaInfoForm() # An unbound form

    return render_to_response(
        'info.html',
        dict(
            spa_name = "Barney's",
            form = form,
            ),
        context_instance=RequestContext(request),
        )


def dongle(request):
    return render_to_response(
        'dongle.html',
        dict(),
        context_instance=RequestContext(request),
        )


def rad(request):
    return render_to_response(
        'rad.html',
        dict(),
        context_instance=RequestContext(request),
        )


def gnarl(request):
    return render_to_response(
        'gnarl.html',
        dict(),
        context_instance=RequestContext(request),
        )

def _keyf((key, value)):
    return key.split('_', 1)[0]

def _timey(t):
    try:
        return datetime.strptime(t, '%H:%M').time().strftime('%H:%M')
    except ValueError:
        pass # i.e. return None

def _times_to_intervals(shift_start, shift_end, lunch_start, lunch_end):
    if not (shift_start and shift_end):
        return ()
    if not (lunch_start and lunch_end):
        return ((shift_start, shift_end),)
    return ((shift_start, lunch_start), (lunch_end, shift_end))

def post_sched(request):
    data = []
    for f in (
        "monday_shift_start","monday_shift_end","monday_lunch_start","monday_lunch_end",
        "tuesday_shift_start","tuesday_shift_end","tuesday_lunch_start","tuesday_lunch_end",
        "wednesday_shift_start","wednesday_shift_end","wednesday_lunch_start","wednesday_lunch_end",
        "thursday_shift_start","thursday_shift_end","thursday_lunch_start","thursday_lunch_end",
        "friday_shift_start","friday_shift_end","friday_lunch_start","friday_lunch_end",
        "saturday_shift_start","saturday_shift_end","saturday_lunch_start","saturday_lunch_end",
        "sunday_shift_start","sunday_shift_end","sunday_lunch_start","sunday_lunch_end",
        ):
        data.append((f, request.POST.get(f)))
    data.sort(key=_keyf)
    res = {}
    for day, times in groupby(data, _keyf):
        res[day] = _times_to_intervals(**dict(
            (key.split('_', 1)[1], _timey(value))
            for key, value in times
            ))
    _P(res)
    return HttpResponse(dumps(res), mimetype="application/json")


{'friday_lunch_end': '',
 'friday_lunch_start': '',
 'friday_shift_end': '',
 'friday_shift_start': '',
 'monday_lunch_end': '',
 'monday_lunch_start': '',
 'monday_shift_end': '',
 'monday_shift_start': '23',
 'saturday_lunch_end': '',
 'saturday_lunch_start': '',
 'saturday_shift_end': '',
 'saturday_shift_start': '',
 'sunday_lunch_end': '',
 'sunday_lunch_start': '',
 'sunday_shift_end': '',
 'sunday_shift_start': '',
 'thursday_lunch_end': '',
 'thursday_lunch_start': '',
 'thursday_shift_end': '',
 'thursday_shift_start': '',
 'tuesday_lunch_end': '',
 'tuesday_lunch_start': 'tert',
 'tuesday_shift_end': 'rt',
 'tuesday_shift_start': 'sdf',
 'wednesday_lunch_end': '',
 'wednesday_lunch_start': '',
 'wednesday_shift_end': '',
 'wednesday_shift_start': ''}
