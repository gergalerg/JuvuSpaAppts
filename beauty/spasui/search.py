from datetime import date, timedelta, datetime
from traceback import print_exc
from spasui.models import get_avails
from beauty.data.treatments import lookup_treatment
from beauty.util.timedate import DATE_FORMAT
from beauty.util.geo import geocode_from_address, grok_address


EXPECTED_FIELDS = [
    'location',
    'treatment',
    'today',
    'tomorrow',
    'thenextday',
    'anotherday',
    ]


def process_POST_params(request):
    data = ensure_fields(dict(request.POST))
    data['lat_long'], data['location_full_text'] = _distance(**data)
    data['dates'] = dates(**data)
    treatment = data['treatment']
    data['treatment_full_text'] = lookup_treatment(treatment) or treatment
    return data


def ensure_fields(D):
    data = dict(
        (name, D.get(name, [None])[0])
        for name in EXPECTED_FIELDS
        )
    if __debug__:
        print data
    return data


def dates(today, tomorrow, thenextday, anotherday, **_):
    '''
    Create a list of datetime.date objects for each of the selected days.

    TODO anotherday should be converted by form validation.
    '''
    days, t, d = [], date.today(), timedelta(days=1)
    if today:
        days.append(t)
    t += d
    if tomorrow:
        days.append(t)
    t += d
    if thenextday:
        days.append(t)
    if anotherday:
        t = datetime.strptime(anotherday, DATE_FORMAT).date()
        days.append(t)
    return days


SF_LOC = {
    'lat': 37.7749295,
    'lng': -122.4194155,
    }


def _distance(location, **_):
    '''
    Do some sort of geo-lookup and figure out a (latitude, longitude)
    pair and a "canonical" display string for the address (or whatever
    was entered.)

    Should possibly raise one of these (unimplemented) exceptions:
        AmbiguousLocationError (too many results)
        NoLocationError (zero results)
        ServiceInterruption (something went wrong, but it's not due to
            user's search.)
    '''
    geo_results = geocode_from_address(location)
    try:
        lat_long, location_full_text = grok_address(**geo_results)
    except:
        lat_long, location_full_text = SF_LOC, location
        print_exc()
    return lat_long, location_full_text


##
##    <QueryDict: {
##        u'csrfmiddlewaretoken': [u'db4187ab0c4fe8ef8859b2e9948ecaba'],
##        u'location': [u'San Francisco'],
##        u'treatment': [u'massage'],
##        u'today': [u'on'],
##        u'anotherday': [u'']
##        }>
##


##
##    {'anotherday': u'11/03/2011',
##     'dates': [datetime.date(2011, 10, 31), datetime.date(2011, 11, 3)],
##     'distance_full_text': 'Where I Left My Heart, CA 94132',
##     'lat_long': (1, 2),
##     'location': u'San Francisco',
##     'thenextday': None,
##     'today': u'on',
##     'tomorrow': None,
##     'treatment': u'massage',
##     'treatment_full_text': 'Massage'}
##


from random import randint


def _fake_appt(n):
    return dict(
        spa = str(n) + "Barney's",
        rating = str(randint(0, 7)) + '/7',
        distance = 2.7 * (10 - n),
        distance_text = str(2.7 * (1 + n)) + ' miles',
        price = '%.2f' % (1001.12 * n),
        )


def _fake_real_appt(av):
    av = av['av']
    distance = randint(1, 300) / 10.
    return dict(
        spa = str(av),
        rating = str(randint(0, 7)) + '/7',
        distance = distance,
        distance_text = str(distance) + ' miles',
        price = '%.2f' % (randint(3, 100) * 10),
        )


def search_for_availabilities(dates, lat_long, treatment, **_):
    print 'search_for_availabilities', dates, lat_long, treatment
    results = []
    for day in dates:
        print day
        day = day.strftime(DATE_FORMAT)
        print treatment, day, '->',
        avs = get_avails(treatment, day)
        print avs
        results.extend(_fake_real_appt(av) for av in avs)
    print results
    print

    if __debug__:
        if not results:
            results = map(_fake_appt, range(7))
    return results
##    return map(_fake_appt, range(7))











