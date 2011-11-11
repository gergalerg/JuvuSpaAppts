from datetime import datetime
from spasui.models import create_availability_with_trenche
from beauty.util import norm_query_dict
from beauty.util.timedate import VALUE, DATE_FORMAT, A_DAY


def create_availabilities(POST):
    for params in process_availability_params(POST):
        yield create_availability(*params)


def process_availability_params(args):
    args = norm_query_dict(args)
    dates, from_time, to_time = dates_from(**args)
    locations, trenches = _get_locations_and_trenches(args)
    for day in dates:
        for location in locations:
            for trenche in trenches:
                yield location, trenche, day, from_time, to_time


def create_availability(location, trenche, day, from_time, to_time):
    '''
    Return a status message or something to indicate whether the
    availability slot was created or not.
    '''
    print "Check location.", location
    print "Check trenche.", trenche
    print "Check day and time", day, from_time, to_time # (for, I dunno, conflicts or something.)
    return create_availability_with_trenche(trenche, day)


def dates_from(from_date, from_time, to_date, to_time, **_):
    fd = datetime.strptime(from_date, DATE_FORMAT)
    td = datetime.strptime(to_date, DATE_FORMAT)
    assert fd <= td, (fd, td)

    dates = []
    while fd <= td:
        dates.append(fd)
        fd += A_DAY

    ft = datetime.strptime(from_time, VALUE).time()
    tt = datetime.strptime(to_time, VALUE).time()

    return dates, ft, tt


def _get_locations_and_trenches(fields):
    locations, trenches = [], []
    for key in fields:
        if key.startswith('loc_'):
            locations.append(key[4:])
        elif key.startswith('trench_'):
            trenches.append(key[7:])
    return locations, trenches
