'''
Render a deal calendar.
'''
from datetime import date, timedelta
from django.template.loader import render_to_string
from beauty.util.timedate import A_DAY, days_since_sunday


class DealCalendar:
    '''
    Render a deal calendar in HTML.
    '''
    # Done as a class and not a function in case we add later the ability
    # to also emit JS and/or CSS as well as teh HTML.

    def __init__(self, day=None):
        self.day = day or date.today()

    def get_table(self):
        days = (
            day.strftime("%d").lstrip('0') if day else ''
            for day in yield_days(self.day)
            )
        return render_to_string(
            'dealcal.html',
            dict(weeks=list(by_sevens(days)))
            )


def by_sevens(days):
    days = list(days)
    while days:
        yield days[:7]
        days = days[7:]


def yield_days(day, how_many_weeks=3):
    assert 1 <= how_many_weeks <= 10, repr(how_many_weeks)

    for _ in xrange(days_since_sunday(day)):
        yield None

    while how_many_weeks:
        yield day
        day += A_DAY
        if day.weekday() == 6:
            how_many_weeks -= 1


# Note: this is a debugging function, not used in production.
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
