'''
Date and time routines and "constants".

(Eventually timezone stuff may live here too.)
'''
from datetime import datetime, timedelta


VALUE = '%H:%M'
TEXT = '%I:%M %p'
DATE_FORMAT = '%m/%d/%Y'


A_DAY = timedelta(days=1)


def datetime_from_hour(hour):
    return datetime.min.replace(hour=hour)


def days_since_sunday(day):
    return (1 + day.weekday()) % 7
