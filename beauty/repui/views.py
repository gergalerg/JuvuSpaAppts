from django.shortcuts import render_to_response
from django.template import RequestContext


TREATMENTS = '''\
Microdermabrasion
Clinical Facial
Chemical Peel
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
Pedicure
Manicure
Sclerotherapy
Endermologie
Herbal Body wrap
Infrared Body wrap
Underarm Rejuvenation
Intense Pulsed Light
Skin Tag Removal
Thermage Skin Tightening
Back Facial
Brazillian Facial
Scrub
Skin Lightening
Tattoo removal
Swedish Massage
Deep Tissue Massage
Prenatal Massage
Thermal Stone Massage
Shiatsu Massage
Reflexology
Laser Hair Removal
Waxing Hair Removal
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
Fraxel'''.splitlines()


def index(request):
    '''
    Home page.
    '''
    return render_to_response(
        'index.html',
        dict(treatments=TREATMENTS),
        context_instance=RequestContext(request),
        )


