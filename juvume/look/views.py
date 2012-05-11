from random import choice, shuffle
from simplejson import dumps
from itertools import cycle
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from juvume.util.results import FAKE_RESULTS


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
        top='19%',
        left='52%',
        color='#C7AA9C',
        ),
    dict(
        image_URL=image_url(3),
        top='38%',
        left='52%',
        color='#6A8CA9',
        ),
    dict(
        image_URL=image_url(4),
        top='40%',
        left='52%',
        color='#E8711F',
        ),
    dict(
        image_URL=image_url(5),
        top='20%',
        left='48%',
        color='#C7452E',
        ),
    dict(
        image_URL=image_url(6),
        top='15%',
        left='45%',
        color='#7B4730',
        ),
    ]


i = cycle(LOGIN_IMAGES).next


def home(request):
    '''
    Login page with rotating background images.
    '''
    if  request.method != 'POST':
        return render_to_response(
            'booking.html',
            i(),
            context_instance=RequestContext(request),
            )

    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user and user.is_active:
        auth.login(request, user)
        return redirect("/Hooray!")
    return redirect('/invalid_login')


def inv(request):
    '''
    Inventory page.
    '''
    r = FAKE_RESULTS.values()
    results = choice(r) if r else []
    shuffle(results)
    return render_to_response(
        'inv.html',
        dict(
            results=dumps(results),
            ),
        context_instance=RequestContext(request),
        )


def book_info(request):
    '''
    capture client's information
    '''
    return render_to_response(
        'book_info_capture.html',
        context_instance=RequestContext(request),
        )


def book_confirm(request):
    '''
    confirm client's information
    '''
    return render_to_response(
        'book_info_confirm.html',
        context_instance=RequestContext(request),
        )


def book_congrats(request):
    '''
    book congratulations
    '''
    return render_to_response(
        'book_congrats.html',
        context_instance=RequestContext(request),
        )

