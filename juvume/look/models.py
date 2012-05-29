from datetime import datetime, timedelta
from juvume.util.results import FAKE_RESULTS


ONE_DAY = timedelta(days=1)
DATE_FORMAT = '%m/%d/%Y'
'05/15/2012'


def get_results(proc, from_date, to_date):
    print 'get_results', proc, from_date, to_date
    days = list(_get_days(from_date, to_date))
    for d in days:
        print '  ', d
    print
    return FAKE_RESULTS.values()[0]


def _get_days(from_date, to_date):
    if from_date:
        from_date = datetime.strptime(from_date, DATE_FORMAT)
    else:
        from_date = datetime.today()
    if to_date:
        to_date = datetime.strptime(to_date, DATE_FORMAT)
    else:
        to_date = from_date
    if to_date < from_date:
        to_date, from_date = from_date, to_date
    while from_date <= to_date:
        yield from_date
        from_date += ONE_DAY
