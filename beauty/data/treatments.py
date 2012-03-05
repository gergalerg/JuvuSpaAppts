'''
Different treatment types grouped by "genus".
'''
from itertools import chain
from difflib import get_close_matches
from simplejson import dumps


TREEd = {'children': [

    {'children': [
        {'supported': False, 'name': 'Theraputic'},
        {'supported': False, 'name': 'Deep Tissue'},
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

TREATMENTS = dict(
	(ch['name'], [gch['name'] for gch in ch['children']])
	for ch in TREEd['children']
	)

SORTED_TREATMENTS = [(k, TREATMENTS[k]) for k in sorted(TREATMENTS)]

ALL_TREATMENTS = list(TREATMENTS) + list(chain(*TREATMENTS.itervalues()))

LOOKUP_TREATMENT = dict(
    (treatment.lower(), treatment)
    for treatment in ALL_TREATMENTS
    )

def lookup_treatment(term):
    terml = term.lower()
    result = LOOKUP_TREATMENT.get(terml)
    if result:
        return result
    results = get_close_matches(terml, list(LOOKUP_TREATMENT))
    if results:
        return LOOKUP_TREATMENT[results[0]]
    # i.e. return None
