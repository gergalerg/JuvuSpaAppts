#!/usr/bin/env python
from operator import attrgetter
from pprint import pprint as P
from datetime import datetime, timedelta
from RDF import Node, Uri, Statement, Storage, Model

OUR_LAND = 'http://choicedocs.com/ref/'
OUR_LAND_URI = Uri(OUR_LAND)
PROVIDER = Uri(OUR_LAND + 'Provider')
TRENCHE = Uri(OUR_LAND + 'Trenche')
TREATMENT = Uri(OUR_LAND + 'Treatment')
PROCTYPE = Uri(OUR_LAND + 'ProcedureType')
CATEGORY = Uri(OUR_LAND + 'Category')
SUBCAT = Uri(OUR_LAND + 'SubCategory')
SUPPORTS = Uri(OUR_LAND + 'SupportsTreatment')
AVAIL = Uri(OUR_LAND + 'AvailabilitySlot')
DATE = Uri(OUR_LAND + 'Date')
WHERE = Uri(OUR_LAND + 'Location')
FROM_TIME = Uri(OUR_LAND + 'from_time')
TO_TIME = Uri(OUR_LAND + 'to_time')
EMPLOYS = Uri(OUR_LAND + 'Employs')
NAME = Uri('http://xmlns.com/foaf/0.1/name')
LABEL = Uri('http://www.w3.org/2000/01/rdf-schema#label')
TYPE = Uri('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
PREFIX = """\
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX cd: <http://choicedocs.com/ref/>
"""

import sys
sys.path.append('/home/sforman/Software/aa-Spa-Stalker')
from beauty.spasui.models import plain_query
import beauty.spasui.models as M

M.M = m = Model(Storage(
    storage_name="file",
    name="testdata.rdf.xml",
    options_string="new='yes',dir='.'",
    ))


@plain_query
def q0(proc, date):
  """
  SELECT distinct ?spa ?time
  WHERE {
      ?t rdf:type cd:Treatment .
      ?t foaf:name "%(proc)s" .
      ?a cd:Treatment ?t .
      ?a cd:Date "%(date)s" .
      ?a cd:Provider ?spa .
      ?a cd:from_time ?time .
  }
  """


@plain_query
def q1(proc, date):
  """
  SELECT distinct ?spa ?time ?t
  WHERE {
      ?pt foaf:name "%(proc)s" .
      ?pt rdf:type cd:ProcedureType .
      ?t cd:SubCategory ?pt .
      ?t rdf:type cd:Treatment .
      ?a cd:Treatment ?t .
      ?a cd:Date "%(date)s" .
      ?a cd:Provider ?spa .
      ?a cd:from_time ?time .
  }
  """

u'Womens Cut', u'03-03-2012'
