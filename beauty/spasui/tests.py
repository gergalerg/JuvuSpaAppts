from datetime import date, time, datetime, timedelta
from django.test import TestCase
from beauty.spasui.availabilities import dates_from
from spasui.search import process_POST_params

# Import these here so the test runner can find them.
from spasui.search_tests import (
    CreateAvailabilitiesTest,
    SearchAvailabilitiesTest,
    )


class process_POST_params_Test(TestCase):

    class FakeRequest:
        def __init__(self):
            self.POST = {
                u'location': [u'San Francisco'],
                u'treatment': [u'massage'],
                u'today': [u'on'],
                u'anotherday': [u'']
                }

    def setUp(self):
        self.fake_request = self.FakeRequest()
        self.today = date.today()

    def test_date_today(self):
        # Find today as per the request params above.
        result = process_POST_params(self.fake_request)
        self.assertEqual(result['dates'], [self.today])

    def test_date_tomorrow(self):
        # Find tomorrow.
        self.fake_request.POST[u'tomorrow'] = [u'on']
        result = process_POST_params(self.fake_request)
        self.assertEqual(
            result['dates'],
            [self.today, self.today + timedelta(days=1)]
            )

    def test_date_tomorrow_without_today(self):
        # Add tomorrow.
        self.fake_request.POST[u'tomorrow'] = [u'on']
        # Remove today.
        del self.fake_request.POST[u'today']
        result = process_POST_params(self.fake_request)
        self.assertEqual(
            result['dates'],
            [self.today + timedelta(days=1)]
            )

    def test_date_another_day(self):
        # Add a specific date (in the past, as the business logic of not
        # allowing appointments in the past will not have been applied
        # yet.
        self.fake_request.POST[u'anotherday'] = [u'11/28/2010']
        result = process_POST_params(self.fake_request)
        self.assertEqual(
            result['dates'],
            [self.today, date(2010, 11, 28)]
            )

    def test_location(self):
        result = process_POST_params(self.fake_request)

        self.assertEqual(
            result['lat_long'],
            {u'lat': 37.7749295, u'lng': -122.4194155}
            )
        self.assertEqual(
            result['location_full_text'],
            u'San Francisco, CA, USA'
            )


class DatesFromTest(TestCase):

    def setUp(self):
        self.post_data = dict(
            sox1='on',
            sox2='on',
            sox3='on',

            trench_B_also='on',
            trench_C='on',

            from_date='11/11/2011',
            from_time='05:00',

            to_date='11/11/2011',
            to_time='21:00',
            )

    def test_same_day(self):
        dates, from_time, to_time = dates_from(**self.post_data)
        self.assertEqual(from_time, time(hour=5))
        self.assertEqual(to_time, time(hour=21))
        self.assertEqual(dates, [datetime(2011, 11, 11)])

    def test_two_days(self):
        self.post_data['to_date'] = '11/12/2011'
        dates, from_time, to_time = dates_from(**self.post_data)
        self.assertEqual(from_time, time(hour=5))
        self.assertEqual(to_time, time(hour=21))
        self.assertEqual(
            dates,
            [
                datetime(2011, 11, 11),
                datetime(2011, 11, 12),
                ]
            )

    def test_three_days(self):
        self.post_data['to_date'] = '11/13/2011'
        dates, from_time, to_time = dates_from(**self.post_data)
        self.assertEqual(from_time, time(hour=5))
        self.assertEqual(to_time, time(hour=21))
        self.assertEqual(
            dates,
            [
                datetime(2011, 11, 11),
                datetime(2011, 11, 12),
                datetime(2011, 11, 13),
                ]
            )

    def test_reversed_days(self):
        self.post_data['from_date'] = '11/13/2011'
        self.assertRaises(
            AssertionError,
            dates_from,
            **self.post_data
            )






