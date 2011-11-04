# API service.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from spasui.api import dispatch


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


def profile(request):
    return render_to_response('profile.html')
