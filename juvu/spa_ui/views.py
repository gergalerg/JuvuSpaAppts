from simplejson import dumps
from django.template import RequestContext
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
    {'name': 'Billy'},
    {'name': 'Bob'},
    {'name': 'Billy Jo Bob'},
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

