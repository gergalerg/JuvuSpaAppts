from django.template import RequestContext
from django.shortcuts import render_to_response
from itertools import cycle


_i = cycle(range(1,7)).next


def next_background_image():
    return 'login_%02i.html' % _i()


def login(request):
    '''
    Login page with rotating background images.
    '''
    return render_to_response(
        next_background_image(),
        context_instance=RequestContext(request),
        )


