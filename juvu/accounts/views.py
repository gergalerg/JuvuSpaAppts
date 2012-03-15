from django.template import RequestContext
from django.shortcuts import render_to_response
from itertools import cycle


def image_url(n):
    return '/static/image/login_%02i.jpg' % (n,)


LOGIN_IMAGES = [
    dict(
        image_URL=image_url(1),
        top='37%',
        left='22%',
        color='#3998C2',
        ),
    dict(
        image_URL=image_url(2),
        top='52%',
        left='19%',
        color='#C7AA9C',
        ),
    dict(
        image_URL=image_url(3),
        top='52%',
        left='38%',
        color='#6A8CA9',
        ),
    dict(
        image_URL=image_url(4),
        top='52%',
        left='50%',
        color='#E8711F',
        ),
    dict(
        image_URL=image_url(5),
        top='48%',
        left='20%',
        color='#C7452E',
        ),
    dict(
        image_URL=image_url(6),
        top='45%',
        left='15%',
        color='#7B4730',
        ),
    ]


_i = cycle(LOGIN_IMAGES).next


def login(request):
    '''
    Login page with rotating background images.
    '''
    return render_to_response(
        'login.html',
        _i(),
        context_instance=RequestContext(request),
        )


