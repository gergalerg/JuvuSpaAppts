from simplejson import dumps
from itertools import cycle
from random import choice, shuffle
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from juvu.util.results import FAKE_RESULTS


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
        top='50%',
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
    results = choice(FAKE_RESULTS.values())
    shuffle(results)
    return render_to_response(
        'inv.html',
        dict(
            results=dumps(results),
            ),
        context_instance=RequestContext(request),
        )


FAKER_RESULTS = dict(
    name = "Barney",
    date_label = "Feburary 72 - 947",
    treatment = "Cupping Therapy",
    day_labels = dict(
        d0="mon 2/20",
        d1="tue 2/21",
        d2="wed 2/22",
        d3="thu 2/23",
        d4="fri 2/24",
        ),
    results = dict(
        morning_1 = [
            dict(time='9:30 am', price=123),
            dict(time='12:00 am', price=12),
            ],
        morning_2 = [],
        morning_3 = [],
        morning_4 = [],
        morning_5 = [],

        afternoon_1 = [
            dict(time='9:30 am', price=123),
            dict(time='12:00 am', price=12),
            ],
        afternoon_2 = [
                             {'price': 52, 'time': '12:15 pm'},
                             {'price': 52, 'time': '12:30 pm'},
                             {'price': 52, 'time': '12:45 pm'},
                             {'price': 52, 'time': '01:00 pm'},
                             {'price': 52, 'time': '01:15 pm'},
                             {'price': 52, 'time': '01:30 pm'},
                             {'price': 52, 'time': '01:45 pm'},
            ],
        afternoon_3 = [],
        afternoon_4 = [],
        afternoon_5 = [],

        evening_1 = [
            dict(time='9:30 am', price=123),
            dict(time='12:00 am', price=12),
            ],
        evening_2 = [
                           {'price': 52, 'time': '03:00 pm'},
                           {'price': 52, 'time': '03:15 pm'},
                           {'price': 52, 'time': '03:30 pm'},
                           {'price': 52, 'time': '04:15 pm'},
                           {'price': 52, 'time': '04:30 pm'},
                           {'price': 52, 'time': '04:45 pm'},
                           {'price': 52, 'time': '05:00 pm'},
                           {'price': 52, 'time': '05:15 pm'},
                           {'price': 52, 'time': '04:00 pm'},
            ],
        evening_3 = [],
        evening_4 = [],
        evening_5 = [],
        ),
    )

def book(request):
    '''
    booking page.
    '''
    return render_to_response(
        'book.html',
        FAKER_RESULTS,
        context_instance=RequestContext(request),
        )

