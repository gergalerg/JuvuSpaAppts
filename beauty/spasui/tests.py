from datetime import date, timedelta
from django.test import TestCase
from spasui.search import process_POST_params


class process_POST_params_Test(TestCase):

    class FakeRequest:
        def __init__(self):
            self.POST = {
                u'csrfmiddlewaretoken': [u'db4187ab0c4fe8ef8859b2e9948ecaba'],
                u'location': [u'San Francisco'],
                u'treatment': [u'massage'],
                u'today': [u'on'],
                u'anotherday': [u'']
                }

    def setUp(self):
        self.fake_request = self.FakeRequest()

    def test_date(self):
        today = date.today()

        # Find today as per the request params above.
        result = process_POST_params(self.fake_request)
        self.assertEqual(result['dates'], [today])

        # Add tomorrow.
        self.fake_request.POST[u'tomorrow'] = [u'on']
        result = process_POST_params(self.fake_request)
        self.assertEqual(
            result['dates'],
            [today, today + timedelta(days=1)]
            )

        # Remove today.
        del self.fake_request.POST[u'today']
        result = process_POST_params(self.fake_request)
        self.assertEqual(
            result['dates'],
            [today + timedelta(days=1)]
            )

        # Add a specific date (in the past, as the business logic of not
        # allowing appointments in the past will not have been applied
        # yet.
        self.fake_request.POST[u'anotherday'] = [u'11/28/2010']
        result = process_POST_params(self.fake_request)
        self.assertEqual(
            result['dates'],
            [today + timedelta(days=1), date(2010, 11, 28)]
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


