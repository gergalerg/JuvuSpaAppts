#!/usr/bin/env python
from csv import DictReader
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
PROCTYPE = Uri(OUR_LAND + 'ProcedureType')
PRICE = Uri(OUR_LAND + 'Price')
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


filename = 'AppointmentsFeb29.csv'
TIME_FORMAT = '%H:%M:%S'
DATE_FORMAT = '%m-%d-%Y'


##T = datetime.strptime(d['Time'], TIME_FORMAT).time()
##D = datetime.strptime(d['Date'], DATE_FORMAT).date()
##t = datetime.combine(D, T)
##print D, T, t


class URICache(dict):

    def get_merchant(self, merchant):
        merch = self.get(merchant)
        if not merch:
            merch = self[merchant] = self.new_merchant_URI(merchant)
        return merch

    def new_merchant_URI(self, merchant):
        return Uri('cd:' + merchant)


Merchants = URICache()
Treatments = {}
ProcedureTypes = {}
Categories = {}

additional_statements = []

def get_category(cat):
    if cat in Categories:
        return Categories[cat]

    c = Categories[cat] = Node()
    additional_statements.extend((
        Statement(c, NAME, cat),
        Statement(c, TYPE, CATEGORY),
        ))

    return c

def get_subtype(st, cat):
    if st in ProcedureTypes:
        return ProcedureTypes[st]

    s = ProcedureTypes[st] = Node()
    additional_statements.extend((
        Statement(s, NAME, st),
        Statement(s, TYPE, PROCTYPE),
        Statement(s, SUBCAT, cat),
        ))

    return s

def get_treatment(cat, subtype, treat):
    if treat in Treatments:
        return Treatments[treat]
    cat = get_category(cat)
    sbt = get_subtype(subtype, cat)
    t = Treatments[treat] = Node()
    additional_statements.extend((
        Statement(t, NAME, treat),
        Statement(t, TYPE, TREATMENT),
        Statement(t, SUBCAT, sbt),
        ))
    return t


def filter_unbooked(I):
    for i, d in enumerate(I):
        if d['Booked'] == 'n' and d['Date'] == '3-2-2012':
            yield d

class DataIterator:

    def __init__(self, filename=filename):
        self.reader = filter_unbooked(DictReader(open(filename)))
        self.merchant_URIs = {}

    def __iter__(self): return self

    def next(self):
        datum = self.reader.next()
        return self.proc(**datum)

    def proc(self,
        Merchant,
        Category,
        ProcedureType,
        Price,
        Booked,
        Time,
        Date,
        SpecificProcedure,
        ):
        res, node = [], Node()

        res.append(
            Statement(node, PROVIDER, Merchants.get_merchant(Merchant))
            )

        # Normalize date.
        Date = datetime.strptime(Date, DATE_FORMAT).date().strftime(DATE_FORMAT)

        res.extend((
            Statement(node, DATE, Date),
            Statement(node, FROM_TIME, Time),
            Statement(node, PRICE, Price.strip()),
            ))

        res.append(
            Statement(node, TREATMENT, get_treatment(Category, ProcedureType, SpecificProcedure))
            )

        return res

m = Model(Storage(
    storage_name="file",
    name="testdata.rdf.xml",
    options_string="new='yes',dir='.'",
    ))

n = 0
def I():
    global n
    for record in DataIterator():
        for statement in record:
            m.add_statement(statement)
            n += 1
    for statement in additional_statements:
        m.add_statement(statement)
        n += 1

print 'loading data'
try:
    I()
finally:
    print 'loaded', n, 'statements'
    m.sync()
    print "sync'd tp disc"

##for n in d:
##    for row in n:
##        print row
##    print
