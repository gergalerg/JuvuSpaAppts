'''
Different treatment types grouped by "genus".
'''
from itertools import chain
from difflib import get_close_matches
from simplejson import dumps


def _str_to_kinds(s):
    '''
    Return a list of strip()'d lines from a multi-line string.
    '''
    return [
        kind.strip()
        for kind in s.splitlines()
        if kind and not kind.isspace()
        ]


TREATMENTS = {

    'Facials': _str_to_kinds('''
        Microdermabrasion
        Clinical Facials
        Chemical Peels
        Organic Treatments
        Hydrating Therapy
        Deep Cleansing Therapy
        Firming and relaxation
        MicroFacial
        Micropeel
        Oxygen Facial
        Aromatherapy
        Pregnancy Facial
        Dysport
        Perlane
        Juvederm
        Restalyne
        Sculptra
        Intentse Pulsed Light
        Laser Resurfacing
        Acne Treatment
        Sublative Rejuvenation
        '''),

    'Hand and Feet': _str_to_kinds('''
        Pedicure
        Medical pedicure
        Manicure
        Medical manicure
        Mani/pedi
        '''),

    'Body Services': _str_to_kinds('''
                Sclerotherapy
        Endermologie
        Body Wrap
                Herbal Body Wrap
                Infrared Body Wrap
        Underarm Rejuvenation
        Intense Pulsed Light
        Skin Tag Removal
        Thermage Skin Tightening
        Back Facial
        Brazillian Facial
        Scrub
        Skin Lightening
        Tattoo removal
        '''),

    'Massage': _str_to_kinds('''
        Swedish
        Deep Tissue
        Prenatal
        Thermal Stone Massage
        Shiatsu
        Reflexology
        '''),

    'Hair Removal': _str_to_kinds('''
        Laser
        Waxing
        Light Heat Therapy
        '''),

    'Skin': _str_to_kinds('''
        BOTOX Cosmetic
        Accent
        Radiesse
        Pixel Skin Treatment
        PhotoDynamic Therapy
        Skin Tightening
        PhotoFacial Elite
        Photorejuvenation
        Fraxel
        Hyaluronic acid
                Restylane
                Hylaform
        '''),

    'Acupuncture': _str_to_kinds('''
        Acupuncture
        Electro Acupuncture
        Cupping Therapy
        Gua Sha Therapy
        Tui Na Therapy
        '''),

    }

SORTED_TREATMENTS = [(k, TREATMENTS[k]) for k in sorted(TREATMENTS)]

OBJ_SORTED_TREATMENTS = [
    dict(name=k, treats=[dict(
        name=t,
        supported=False,
        sub=True,
        ) for t in TREATMENTS[k]])
    for k in sorted(TREATMENTS)
    ]

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


##TREEd = {
##    'children': [
##        {
##            'children': [
##                {'name': 'Theraputic', 'supported': False},
##                {'name': 'Deep Tissue', 'supported': False},
##                {'name': 'Hot Stone', 'supported': False},
##                {'name': 'Reflexology', 'supported': False},
##                {'name': 'Happy Ending', 'supported': False}
##                ],
##            'name': 'Massage'
##            },
##
##
##
##
##        {   'name': 'Face',
##            'children': [
##
##                {'name': 'Facials', 'supported': False},
##
##                {'name': 'Lashes & Brows', 'children': [
##                    {'name': 'Lash Extensions', 'supported': False},
##                    {'name': 'Lash Tinting', 'supported': False},
##                    {'name': 'Brow Tinting', 'supported': False}
##                    ]},
##
##                {'name': 'Peels', 'children': [
##                     {'name': 'Microdermabrasion', 'supported': False},
##                     {'name': 'Chemical Peels', 'supported': False}
##                     ]},
##
##                {'name': 'Medi', 'children': [
##                      {'name': 'Facial Fillers', 'supported': False},
##                      {'name': 'Laser Facials', 'supported': False},
##                      {'name': 'BOTOX', 'supported': False}
##                      ]},
##
##                {'name': 'Make Up', 'children': [
##                    {'name': 'Application', 'supported': False},
##                    {'name': 'Permanent Makeup', 'supported': False}
##
##                    ]},
##        ]},
##
##
##        {'children': [
##            {'name': "Women's Cut", 'supported': False},
##            {'name': 'Conditioning Treatments', 'supported': False},
##            {'name': 'Blowout', 'supported': False},
##            {'name': 'Updo', 'supported': False},
##            {'name': 'Extensions', 'supported': False},
##            {'name': 'Straightening', 'supported': False},
##            {'name': "Men's Cut", 'supported': False}
##            ],
##        'name': 'Hair'
##         },
##
##
##
##
##  
##              {'children': [{'name': 'Pedicure', 'supported': False},
##                            {'name': 'Manicure', 'supported': False},
##                            {'name': 'Mani/pedi', 'supported': False},
##                            {'name': 'Polish Change', 'supported': False},
##				{'name': 'Gels', 'supported': False},                            	
##				{'name': 'Acrylics', 'supported': False}],
##               'name': 'Nails'},
##
##
##
##              {'children': [
##                  {'name': 'Waxing',
##                   'children': [
##                       {'name': 'Brows', 'supported': False},
##                       {'name': 'Bikini/Brazilian', 'supported': False},
##                       {'name': 'Face', 'supported': False},
##                       {'name': 'Body', 'supported': False},
##                       {'name': "Men's", 'supported': False}
##                       ]
##                   },
##                  {'name': 'Laser', 'supported': False},
##                  {'name': 'Threading', 'supported': False},
##                  {'name': 'Sugaring', 'supported': False},
##                  {'name': 'Electrolysis', 'supported': False}
##                  ],
##               'name': 'Hair Removal'
##               },
##
##
##              {'children': [{'name': 'Yoga', 'supported': False},
##                            {'name': 'Pilates', 'supported': False},
##                            {'name': 'Cross Training Classes', 'supported': False},
##                            {'name': 'Cycling Classes', 'supported': False},
##                            {'name': 'TRX', 'supported': False},
##                            {'name': 'Flexibility/Stretching Classes', 'supported': False},
##                            {'name': 'Outdoor Bootcamp', 'supported': False},
##                            {'name': 'Abs & Targeted Area Classes', 'supported': False},
##                            {'name': 'Personal Training', 'supported': False}],
##               'name': 'Fitness'},
##
##
## 		{'children': [{'name': 'Chiropractic', 'supported': False},
##                            {'name': 'Actupuncture', 'supported': False},
##                            {'name': 'Colonics', 'supported': False},
##                            {'name': 'Weight Loss', 'supported': False}],
##               'name': 'Alternative Wellness'},
##
##
##  		{'children': [
##                    {'name': 'Tanning', 'supported': False, 'children': [
##                        {'name': 'Spray Tan', 'supported': False},
##                        {'name': 'Tanning Beds', 'supported': False}
##                        ]
##                     },
##                    {'name': 'Scrubs', 'supported': False},
##                    {'name': 'Wraps', 'supported': False},
##                    {'name': 'Back Facials', 'supported': False},
##                    ],
##                 'name': 'Body Treatments',
##                 },
##
##		 {'children': [
##                     {'name': 'Cleaning', 'supported': False},
##                     {'name': 'Whitening', 'supported': False}
##                     ],
##                  'name': 'Dental'
##                  }],
##    'name': 'Enjoy'}
TREEd = {
    'name': 'Enjoy',
    'children': [
        {
            'name': treatment,
            'children': [{
                'name': kind,
                'supported': False,
                } for kind in kinds],
            }
        for treatment, kinds in SORTED_TREATMENTS
        ],
    }
##TREEd['children'][0]['children'][0]['children'] = [
##    {
##                'name': 'hair',
##                'supported': False,
##                },
##    {
##                'name': 'nails',
##                'supported': False,
##                }]
TREE = dumps(TREEd, indent=2)
