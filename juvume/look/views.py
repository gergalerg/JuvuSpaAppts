from random import choice, shuffle
from simplejson import dumps
from itertools import cycle
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from juvume.look.models import get_results
from juvume.util.results import FAKER_RESULTS
from juvume.util.login_images import LOGIN_IMAGES





def home(request):
    '''
    Login page with rotating background images.
    '''
    i = cycle(LOGIN_IMAGES).next
    if request.method != 'POST':
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
    if request.method == 'POST':
        results = get_results(
            proc=request.POST.get('proc'),
            from_date=request.POST.get('from_date'),
            to_date=request.POST.get('to_date'),
            )
    else:
        results = get_results(None, None, None)
    shuffle(results)
    return render_to_response(
        'inv.html',
        dict(
            results=dumps(results),
            ),
        context_instance=RequestContext(request),
        )

def book(request):
    '''
    booking page.
    '''
    if request.method == 'POST':
        results = get_results(None, None, None)

    return render_to_response(
        'book.html',
        {'name': 'name'},
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

