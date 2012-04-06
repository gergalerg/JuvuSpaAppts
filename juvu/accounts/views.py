from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from booking.views import i

def login(request):
    '''
    Login page with rotating background images.
    '''
    return render_to_response(
        'login.html',
        i(),
        context_instance=RequestContext(request),
        )
