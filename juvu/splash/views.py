# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from juvu.splash.models import proc_email


def splash(request):
    '''
    Splash page.
    '''
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
        proc_email(email_addy)
##        form = RecordEmailForm(request.POST)
##        if form.is_valid():
##            email_addy = form.cleaned_data['record_email']
    return redirect(reverse("thanks"))


def inv(request):
    '''
    Inventory page.
    '''
    return render_to_response(
        'inv.html',
        {'a_var': "Hi!"},
        context_instance=RequestContext(request),
        )

def boo(request):
    '''
    booking page.
    '''
    return render_to_response(
        'boo.html',
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