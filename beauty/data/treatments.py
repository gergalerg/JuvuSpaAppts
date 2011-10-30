'''
Different treatment types grouped by "genus".
'''
from itertools import chain
from difflib import get_close_matches


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
        Juvederm
        Radiesse
        Perlane
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


##    '''\
##    Microdermabrasion
##    Clinical Facial
##    Chemical Peel
##    Hydrating Therapy
##    Deep Cleansing Therapy
##    Firming and relaxation
##    MicroFacial
##    Micropeel
##    Oxygen Facial
##    Aromatherapy
##    Pregnancy Facial
##    Dysport
##    Perlane
##    Juvederm
##    Restalyne
##    Sculptra
##    Intentse Pulsed Light
##    Laser Resurfacing
##    Acne Treatment
##    Sublative Rejuvenation
##    Pedicure
##    Manicure
##    Sclerotherapy
##    Endermologie
##    Herbal Body wrap
##    Infrared Body wrap
##    Underarm Rejuvenation
##    Intense Pulsed Light
##    Skin Tag Removal
##    Thermage Skin Tightening
##    Back Facial
##    Brazillian Facial
##    Scrub
##    Skin Lightening
##    Tattoo removal
##    Swedish Massage
##    Deep Tissue Massage
##    Prenatal Massage
##    Thermal Stone Massage
##    Shiatsu Massage
##    Reflexology
##    Laser Hair Removal
##    Waxing Hair Removal
##    BOTOX Cosmetic
##    Accent
##    Juvederm
##    Radiesse
##    Perlane
##    Pixel Skin Treatment
##    PhotoDynamic Therapy
##    Skin Tightening
##    PhotoFacial Elite
##    Photorejuvenation
##    Fraxel'''.splitlines()
