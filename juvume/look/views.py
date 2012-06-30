from random import choice, shuffle
from simplejson import dumps
from itertools import cycle
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from django.contrib import auth
from look.models import Availability
from look.models import Category
from look.models import Procedure
import datetime

def image_url(n):
    return '/static/image/login_%02i.jpg' % (n,)

def home(request):
    '''
    Login page with rotating background images.
    '''
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
        return redirect("/look/#service")
    return redirect('/invalid_login')

def hooray(request):
    # login bypasses this and returns /look/#service
    return render_to_response(
            'book.html',
            context_instance=RequestContext(request),
            )



def inv(request):
    '''
    Inventory page.
    '''
    #if request.method == 'POST':
    #    results = get_results(
	#   proc=request.POST.get('proc'),
	#   from_date=request.POST.get('from_date'),
	#   to_date=request.POST.get('to_date'),
	#  )
   	# else:
    #   results = get_results(None, None, None)
    #shuffle(results)
    

    #new by DC

    print request.POST.get('proc')
    print request.POST.get('from_date')
    print request.POST.get('to_date')

    #cat = Category.objects.filter(category=request.POST.get('proc'))
    #print cat.count()
    #proc = cat.procedure_set.all();
    #avail = cat.Availability_set.all()
    avail = Availability.objects.filter(appt_date=datetime.datetime.today())
    price =  Availability.objects.filter(appt_date=datetime.datetime.today()).values_list('base_price').distinct().order_by('base_price')

    json_result = "["
    
    for each_price in price:
    	json_result += "{base_price:" + str(each_price[0]) + ",appts:["
    	avail = Availability.objects.filter(appt_date=datetime.datetime.today()).filter(base_price=each_price[0])
    	for each_avail in avail:
    		#print each_avail.base_price,each_avail.proc_name
    		json_result += "{spa_name:'" + each_avail.spa.name + "',timeslot:'" + str(each_avail.timeslot) + "',duration:'" + str(each_avail.duration)+ "'}"	
    	json_result += "]},"		
    json_result += "]"	
    
    x=dict()		
    x['proc'] = request.POST.get('proc')
    x['date'] = datetime.datetime.now()
  #  x['avail'] = avail
  #  x['price'] = price 
    x['json_result'] = json_result
    
    '''
    END DC
    '''
    print json_result
    print x['proc']
        
    return render_to_response(
        'inv.html',
        x,
        context_instance=RequestContext(request),
        )    
        
        
        

def book(request):
    '''
    booking page.
    '''
    results = FAKER_RESULTS
    if request.method == 'POST':
        FAKER_RESULTS['treatment'] = request.POST['name']
       # {'treatment': request.POST['name']}
                
        # treatment = request.POST['name']
    else:
        return HttpResponseRedirect('inv')
    return render_to_response(
        'book.html',
        results,
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

