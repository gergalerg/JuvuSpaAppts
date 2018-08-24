from collections import defaultdict
from django.shortcuts import render_to_response
from django.template import RequestContext
from spasui.models import prepare_trenche_data
from beauty.data.treatments import SORTED_TREATMENTS


def index(request):
    '''
    Rep UI page.
    '''
    return render_to_response(
        'index.html',
        dict(
            treatments=SORTED_TREATMENTS,
            trenches=prepare_trenche_data(),
            ),
        context_instance=RequestContext(request),
        )



