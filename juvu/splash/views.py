import logging
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from juvu.splash.models import proc_email
from juvu.util.spreadlogger import SpreadHandler
from django.conf import settings


# Set up spread logging.
def _f(log):
    handler = SpreadHandler(
        spreadd=settings.SPREAD,
        group=settings.SP_GROUP,
        user=settings.SP_UNAME,
        )
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    handler.setFormatter(formatter)
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)

_log = logging.getLogger("splash")
_f(_log)


def splash(request):
    '''
    Splash page.
    '''
    _log.info(
        " | ".join(["%r"] * 5),
        request.META['REMOTE_ADDR'],
        request.META['REMOTE_HOST'],
        request.get_host(),
        request.META['HTTP_USER_AGENT'],
        request.META.get('HTTP_REFERER', '[no HTTP_REFERER]'),
        )
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request),
        )


def thanks(request):
    '''
    After-Splash page.
    '''
    return render_to_response(
        'redirect.html',
        context_instance=RequestContext(request),
        )


def record_email(request):
    '''
    Record emails from the splash page.
    '''
    if request.method == 'POST':
        email_addy = request.POST['record_email']
        proc_email(email_addy, _log)
    return redirect(reverse("thanks"))

def calendar(request):
    '''
    calendar page.
    '''
    return render_to_response(
        'calendar.html',
        context_instance=RequestContext(request),
        )

def bid(request):
    '''
    bid page.
    '''
    return render_to_response(
        'bid.html',
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

def bid_info(request):
    '''
    capture client's information
    '''
    return render_to_response(
        'bid_info_capture.html',
        context_instance=RequestContext(request),
        )

def bid_confirm(request):
    '''
    confirm client's information
    '''
    return render_to_response(
        'bid_info_confirm.html',
        context_instance=RequestContext(request),
        )

def bid_congrats(request):
    '''
    bid congratulations
    '''
    return render_to_response(
        'bid_congrats.html',
        context_instance=RequestContext(request),
        )
