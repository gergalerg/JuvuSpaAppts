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

def calendar(request):
    '''
    calendar page.
    '''
    return render_to_response(
        'calendar.html',
        context_instance=RequestContext(request),
        )

def inv(request):
    '''
    Inventory page.
    '''
    return render_to_response(
        'inv.html',
        context_instance=RequestContext(request),
        )

def book(request):
    '''
    booking page.
    '''
    return render_to_response(
        'book.html',
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
        
def merchant(request):
    '''
    merchant page - about.
    '''
    return render_to_response(
        'merchant_about.html',
        context_instance=RequestContext(request),
        )

def merchant_reviews(request):
    '''
    merchant page - user review.
    '''
    return render_to_response(
        'merchant_reviews.html',
        context_instance=RequestContext(request),
        )

def merchant_services(request):
    '''
    merchant page - services.
    '''
    return render_to_response(
        'merchant_services.html',
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



















