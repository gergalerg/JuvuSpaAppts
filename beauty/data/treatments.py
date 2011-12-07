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


_tree_form_treatments = {
    'name': 'Enjoy',
    'children': [
        {
            'name': treatment,
            'children': [{'name': kind} for kind in kinds],
            }
        for treatment, kinds in SORTED_TREATMENTS
        ],
    }
TREE = dumps(_tree_form_treatments, indent=2)
