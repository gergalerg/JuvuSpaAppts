from collections import defaultdict
from django.shortcuts import render_to_response
from django.template import RequestContext
from spasui.models import prepare_trenche_data
from beauty.data.treatments import TREATMENTS


_t = [(k, TREATMENTS[k]) for k in sorted(TREATMENTS)]


def index(request):
    '''
    Rep UI page.
    '''
    return render_to_response(
        'index.html',
        dict(
            treatments=_t,
            trenches=prepare_trenche_data(),
            ),
        context_instance=RequestContext(request),
        )



