# API service.
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
