from collections import defaultdict
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from repui.api import dispatch
from repui.models import get_trenche_support


def _json_boolean(n):
    return ("false", "true")[bool(n)]


def iapi(request):
    if __debug__:
        print request.POST
    res = dispatch(**request.POST)
    return HttpResponse(
        _json_boolean(res),
        mimetype="application/json",
        )


def _str_to_kinds(s):
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


_t = [(k, TREATMENTS[k]) for k in sorted(TREATMENTS)]


def _prepare_trenche_data():
    d = defaultdict(list)
    for r in get_trenche_support():
        d[str(r['trenchelabel'])].append(str(r['treatmentname']))
    for default_trenche in "ABC":
        if default_trenche not in d:
            d[default_trenche] # force appearance of key.
    return [
        (k, sorted(d[k]))
        for k in sorted(d)
        ]


def index(request):
    '''
    Home page.
    '''
    return render_to_response(
        'index.html',
        dict(
            treatments=_t,
            trenches=_prepare_trenche_data(),
            ),
        context_instance=RequestContext(request),
        )


