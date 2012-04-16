from simplejson import dumps, loads
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from spa_ui.forms import SpaInfoForm


TREEd = {'children': [

    {'children': [
        {'supported': False, 'name': 'Theraputic'},
        {'supported': False, 'name': 'Thai'},
        {'supported': False, 'name': 'Hot Stone'},
        {'supported': False, 'name': 'Reflexology'},
        ],
     'name': 'Massage',
     'amenities': [
         'Lockers/Robes',
         'Steam/Sauna',
         'Showers',
         'Pool',
         ]
     },

    {'name': 'Face',
     'children': [
        {'supported': False, 'name': 'Facials'},
        {'name': 'Lashes & Brows', 'children': [
            {'supported': False, 'name': 'Lash Extensions'},
            {'supported': False, 'name': 'Lash Tinting'},
            {'supported': False, 'name': 'Brow Tinting'}
            ]
         },
        {'name': 'Peels', 'children': [
            {'supported': False, 'name': 'Microdermabrasion'},
            {'supported': False, 'name': 'Chemical Peels'}
            ]
         },
        {'name': 'Medi', 'children': [
            {'supported': False, 'name': 'Facial Fillers'},
            {'supported': False, 'name': 'Laser Facials'},
            {'supported': False, 'name': 'BOTOX'}
            ]
         },
        {'name': 'Make Up', 'children': [
            {'supported': False, 'name': 'Application'},
            {'supported': False, 'name': 'Permanent Makeup'}
            ]
         }
        ],
     'amenities': ['Lockers/Robes']
     },

    {'children': [
        {'supported': False, 'name': 'Womens Cut'},
        {'supported': False, 'name': 'Conditioning Treatments'},
        {'supported': False, 'name': 'Blowout'},
        {'supported': False, 'name': 'Updo'},
        {'supported': False, 'name': 'Extensions'},
        {'supported': False, 'name': 'Straightening'},
        {'supported': False, 'name': 'Mens Cut'}
        ],
     'name': 'Hair',
     'amenities': ['Wine']
     },

    {'children': [
        {'name': 'Waxing', 'children': [
            {'supported': False, 'name': 'Brows/Face'},
            {'supported': False, 'name': 'Bikini/Brazilian'},
            {'supported': False, 'name': 'Body'},
            {'supported': False, 'name': "Mens"}
            ]
         },
        {'supported': False, 'name': 'Laser'},
        {'supported': False, 'name': 'Threading'},
        {'supported': False, 'name': 'Sugaring'},
        {'supported': False, 'name': 'Electrolysis'}
        ],
     'name': 'Hair Removal',
     'amenities': ['Wine']
     },

    {'children': [
        {'supported': False, 'name': 'Pedicure'},
        {'supported': False, 'name': 'Manicure'},
        {'supported': False, 'name': 'Mani/pedi'},
        {'supported': False, 'name': 'Polish Change'},
        {'supported': False, 'name': 'Gels'},
        {'supported': False, 'name': 'Acrylics'}
        ],
     'name': 'Nails',
     'amenities': ['Wine']
     },

    {'children': [
        {'supported': False, 'name': 'Yoga'},
        {'supported': False, 'name': 'Pilates'},
        {'supported': False, 'name': 'Cross Training Classes'},
        {'supported': False, 'name': 'Cycling Classes'},
        {'supported': False, 'name': 'TRX'},
        {'supported': False, 'name': 'Flexibility/Stretching Classes'},
        {'supported': False, 'name': 'Outdoor Bootcamp'},
        {'supported': False, 'name': 'Abs & Targeted Area Classes'},
        {'supported': False, 'name': 'Personal Training'}
        ],
     'name': 'Fitness',
     'amenities': [
         'Lockers/Robes',
         'Steam/Sauna',
         'Showers',
         'Pool',
         ]
     },

    {'children': [
        {'supported': False, 'name': 'Chiropractic'},
        {'supported': False, 'name': 'Actupuncture'},
        {'supported': False, 'name': 'Colonics'},
        {'supported': False, 'name': 'Weight Loss'}
        ],
     'name': 'Alternative Wellness',
     'amenities': []
     },

    {'children': [
        {'supported': False, 'name': 'Tanning', 'children': [
            {'supported': False, 'name': 'Spray Tan'},
            {'supported': False, 'name': 'Tanning Beds'}
            ]
         },
        {'supported': False, 'name': 'Scrubs'},
        {'supported': False, 'name': 'Wraps'},
        {'supported': False, 'name': 'Back Facials'}
        ],
     'name': 'Body Treatments',
     'amenities': ['Showers']
     },

    {'children': [
        {'supported': False, 'name': 'Cleaning'},
        {'supported': False, 'name': 'Whitening'}
        ],
     'name': 'Dental',
     'amenities': []
     }

    ],
         'name': 'Enjoy'
         }


TREE = dumps(TREEd, indent=2)


STAFF = [
    ]


def home(request):
    '''
    '''
    return render_to_response(
        'spa_home.html',
        dict(
            form=SpaInfoForm(),
            tree_data=TREE,
            staff=STAFF,
            ),
        context_instance=RequestContext(request),
        )


def cal(request):
    '''
    '''
    return render_to_response(
        'cal.html',
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
       

from pprint import pprint
from datetime import datetime
import pickle
DAY_LABEL = '%m-%d-%Y'


THE_FAKE_DB = {}
_ew = []
_all = [dict(
            name="Spa Name",
            results=_ew,
            )]

def proc_it(start, end, procs, **huh):
##    if not procs:
##        return
    start = datetime.fromtimestamp(start/1000)
    end = datetime.fromtimestamp(end/1000)
    print start, end
    day_label = start.date().strftime(DAY_LABEL)
    ressy = THE_FAKE_DB.get(day_label)
    if ressy is None:
        ressy = THE_FAKE_DB[day_label] = _all
    _ew.extend(procs)
    pprint(THE_FAKE_DB)
    pickle.dump(THE_FAKE_DB, open('/tmp/data',  'w'))


def fooey(request):
    '''
    merchant page - services.
    '''
    pprint(request.POST.keys()[0])
    data = request.POST.keys()[0]
    data = loads(data)
    pprint(data)
    proc_it(**data)
    
    return HttpResponse("Form submitted")
       







