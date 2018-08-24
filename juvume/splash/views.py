import logging
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from juvume.splash.models import proc_email
from juvume.util.spreadlogger import SpreadHandler
from django.conf import settings
from django.views.generic.simple import direct_to_template



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
        request.META.get('REMOTE_HOST', '[no REMOTE_HOST]'),
        request.get_host(),
        request.META['HTTP_USER_AGENT'],
        request.META.get('HTTP_REFERER', '[no HTTP_REFERER]'),
        )
    return direct_to_template(request, template='index.html')
#    return render_to_response(
#        'index.html',
#        context_instance=RequestContext(request),
#       )


def thanks(request):
    '''
    After-Splash page.
    '''
    return render_to_response(
        'thanks.html',
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

