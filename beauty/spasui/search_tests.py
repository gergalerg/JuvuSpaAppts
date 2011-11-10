try:
    from RDF import Storage, Model, Statement
except ImportError:
    from fake_rdf import Storage, Model, Statement
from django.test import TestCase
from django.conf import settings
from spasui.models import (
    add_treatment_to_trenche,
    create_availability_with_trenche,
    get_trenche_support,
    get_avails,
    )
from beauty.util.URIs import TYPE, DATE, AVAIL
import spasui.models


class ModelMixin:

    def setUp(self):
        self._M = spasui.models.M
        spasui.models.M = Model(Storage(**settings.TRIPLE_STORES['default']))

    def tearDown(self):
        spasui.models.M = self._M


class CreateAvailabilitiesTest(ModelMixin, TestCase):
    """
    Tests the functionality related to Availabilities.
    """

    def testAddTreatmentToTrenche(self):
        add_treatment_to_trenche('Banana Slug Dip', 'A')

        result = get_trenche_support()
        self.assertEqual(len(result), 1)

        result = result[0]
        self.assertEqual(str(result['treatmentname']), 'BananaSlugDip')
        self.assertEqual(str(result['trenchelabel']), 'A')

    def testCreateAvailabilityWithUnknownTrenche(self):
        result = create_availability_with_trenche("A", "")
        self.assert_(not result)
        self.assertEqual(list(spasui.models.M.as_stream()), [])

    def testCreateAvailabilityWithTrenche(self):
        add_treatment_to_trenche('Banana Slug Dip', 'A')
        result = create_availability_with_trenche("A", "11/03/2011")
        self.assert_(Statement(result, TYPE, AVAIL) in spasui.models.M)
        self.assert_(Statement(result, DATE, "11/03/2011") in spasui.models.M)


class SearchAvailabilitiesTest(ModelMixin, TestCase):
    """
    Tests the functionality related to searching Availabilities.
    """

    def test_get_avails(self):
        add_treatment_to_trenche('Banana Slug Dip', 'A')
        result = create_availability_with_trenche("A", "11/03/2011")

        also_result = get_avails('BananaSlugDip', "11/03/2011")

        self.assertEqual(len(also_result), 1)
        self.assertEqual(also_result[0]['av'], result)

    def test_get_avails_one_day(self):
        add_treatment_to_trenche('Banana Slug Dip', 'A')
        resultA = create_availability_with_trenche("A", "11/03/2011")
        resultB = create_availability_with_trenche("A", "11/04/2011")

        also_result = get_avails('BananaSlugDip', "11/03/2011")
        self.assertEqual(len(also_result), 1)
        self.assertEqual(also_result[0]['av'], resultA)

        also_result = get_avails('BananaSlugDip', "11/04/2011")
        self.assertEqual(len(also_result), 1)
        self.assertEqual(also_result[0]['av'], resultB)


##
##        s = Statement(result, DATE, None)
##        print '- - - - - - - - - - - - - - - - '
##        for stmt in spasui.models.M.find_statements(s):
##            print stmt
##        print '- - - - - - - - - - - - - - - - '






