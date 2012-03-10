from django.template import RequestContext
from django.shortcuts import render_to_response

def splash(request):
    '''
    Splash page.
    '''
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request),
        )
