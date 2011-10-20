from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    '''
    Home page.
    '''
    c = {}
    return render_to_response(
        'index.html',
        c,
        context_instance=RequestContext(request),
        )


