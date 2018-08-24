#!/usr/bin/env python
'''
Generate an HTML select element for times of day.
'''
from datetime import datetime, time, timedelta
from beauty.util.timedate import (
    VALUE,
    TEXT,
    DATE_FORMAT,
    A_DAY,
    datetime_from_hour,
    )


def HTML_select(name, hour, minutes, last=datetime_from_hour(21)):
    t = datetime_from_hour(hour)
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


if __name__ == '__main__':
    print HTML_select('from_time', 5, 15)
