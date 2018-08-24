from datetime import datetime
from juvu.util.LIST import results


IN_VALUE = '%H:%M:%S'
OUT_VALUE = '%I:%M %p'
DATE_FORMAT = '%m-%d-%Y'
DAY_LABEL = '%a %m/%d'
NOON = datetime.strptime('12:00:00', IN_VALUE).time()
AFTERNOON = datetime.strptime('14:30:00', IN_VALUE).time()


def format_time(t):
    return t.strftime(OUT_VALUE).lower()

def k(date, price, spa, spec_treat, time):
    return dict(
        time = datetime.strptime(time, IN_VALUE).time(),
        price = int(price),
        date = datetime.strptime(date, DATE_FORMAT).date(),
        spec_treat = spec_treat,
        spa = spa,
        )

class ResultsConverter:

    def __init__(self, treatment, spa):
        self.dates = {}
        self.treatment = treatment
        self.spa = spa

    def filter(self, stream):
        for result in stream:
            if result['spec_treat'] != self.treatment:
                continue
            if result['spa'] != self.spa:
                continue
            self.process_one(result)

    def process_one(self, datum):
        datum = k(**datum)
        p = self.get_date(datum['date'])
        t = datum['time']
        if t < NOON:
            p = p['morning']
        elif t < AFTERNOON:
            p = p['afternoon']
        else:
            p = p['evening']
        p.append(dict(
            time=format_time(t),
            price=datum['price'],
            ))

    def get_date(self, date):
        date = date.strftime(DAY_LABEL)
        if date in self.dates:
            return self.dates[date]
        d = self.dates[date] = dict(
            morning=[],
            afternoon=[],
            evening=[],
            )
        return d

    
R = ResultsConverter('Haircut and Style - Junior Lev', 'cd:Cinta')
print 'R.filter(results)'

