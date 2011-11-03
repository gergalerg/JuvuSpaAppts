'''
Rough draft of calendar rendering.
'''

##from calendar import HTMLCalendar
##print HTMLCalendar(6).formatmonth(2011, 11)

from pprint import pprint
from datetime import date, timedelta


def by_sevens(days):
    days = list(days)
    while days:
        yield days[:7]
        days = days[7:]


A_DAY = timedelta(days=1)

D = [
    'mon', # 1
    'tues', # 2
    'wed',
    'thurs',
    'fri',
    'sat',
    'sun',
    ]

d = date.today()

def days_since_sunday(day):
    return (1 + day.weekday()) % 7

def yield_days(day, how_many_weeks=3):
    assert 1 <= how_many_weeks <= 10, repr(how_many_weeks)

    for _ in xrange(days_since_sunday(day)):
        yield None

    while how_many_weeks:
        yield day
        day += A_DAY
        if day.weekday() == 6:
            how_many_weeks -= 1

##for _ in range(7):
##    d += A_DAY
##    print d.strftime("%A %d. %B %Y")
##    for day in yield_days(d):
##        print day, day and day.strftime("%A %d. %B %Y")
##    print 

def tableize(day):
    yield '''\
<table border="0" cellpadding="0" cellspacing="0" class="month">
<thead>
<tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>
</thead>
<tbody>'''
    for week in by_sevens(yield_days(day)):
        yield '<tr class="week">'
        for day in week:
            day = day.strftime("%d").lstrip('0') if day else ''
            yield '<td class="day">%s</td>' % (day,)
        yield '</tr>'
    yield '''\
</tbody>
</table>
'''

if __name__ == '__main__':
    print '\n'.join(tableize(date.today()))
