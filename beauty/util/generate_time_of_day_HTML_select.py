#!/usr/bin/env python
'''
Generate an HTML select element for times of day.
'''
from datetime import datetime, time, timedelta


VALUE, TEXT = '%H:%M', '%I:%M %p'
DATE_FORMAT = '%m/%d/%Y'


_A_DAY = timedelta(days=1)


def _t(hour):
    return datetime.min.replace(hour=hour)


def HTML_select(name, hour, minutes, last=_t(21)):
    t = _t(hour)
    d = timedelta(minutes=minutes)
    res = ['<select name="%s">' % (name,)]
    while t <= last:
        tt = t.time()
        res.append(
            '<option value="%s">%s</option>' %
            (
                tt.strftime(VALUE),
                tt.strftime(TEXT).lstrip('0')
                )
            )
        t += d
    res.append('</select>')
    return '\n'.join(res)


def dates_from(
    from_date='11/11/2011',
    from_time='05:00',
    to_date='11/11/2011',
    to_time='21:00',
    **_
    ):
    fd = datetime.strptime(from_date, DATE_FORMAT)
    td = datetime.strptime(to_date, DATE_FORMAT)
    assert fd <= td, (fd, td)

    dates = []
    while fd <= td:
        dates.append(fd)
        fd += _A_DAY

    ft = datetime.strptime(from_time, VALUE).time()
    tt = datetime.strptime(to_time, VALUE).time()

    return dates, ft, tt


if __name__ == '__main__':
    print HTML_select('from_time', 5, 15)
