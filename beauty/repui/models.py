from django.conf import settings
from RDF import (
  Storage,
  Model,
  Statement,
  Uri,
  Node,
  Parser,
  Query,
  SPARQLQuery,
  Serializer,
  )


OUR_LAND = 'http://choicedocs.com/ref/'
OUR_LAND_URI = Uri(OUR_LAND)


NAME = Uri(OUR_LAND + 'name')
PROVIDER = Uri(OUR_LAND + 'Provider')
TRENCHE = Uri(OUR_LAND + 'Trenche')
TREATMENT = Uri(OUR_LAND + 'Treatment')
SUPPORTS = Uri(OUR_LAND + 'SupportsTreatment')


LABEL = Uri('http://www.w3.org/2000/01/rdf-schema#label')
TYPE = Uri('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')


M = Model(Storage(**settings.TRIPLE_STORES['default']))


def _query(sparql, **args):
  return list(SPARQLQuery(str(sparql % args)).execute(M))


def provider_named(name):
  return _query("""\
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cd: <http://choicedocs.com/ref/>
SELECT distinct ?a
WHERE {
    ?a rdf:type cd:Provider .
    ?a cd:name "%(name)s" .
}
  """,
  name=name,
  )


def add_thing(name, label, kind):
  thing = Node()
  f = lambda p, o: Statement(thing, p, o)
  for s in (
    f(TYPE, kind),
    f(NAME, name),
    f(LABEL, label),
    ):
    M.add_statement(s)
  return thing


def add_provider(name, label):
  return add_thing(name, label, PROVIDER)


def add_treatment(name, label=None):
  if label is None:
    label, name = name, ''.join(name.split())
  return add_thing(name, label, TREATMENT)


def add_trenche(name):
  return add_thing(name, name, TRENCHE)


def add_treatment_to_trenche(treatment, trenche):
  T = get_treatment_from_label(treatment)
  treatment = T[0] if T else add_treatment(treatment)

  T = get_trenche_from_label(trenche)
  trenche = T[0] if T else add_trenche(trenche)

  s = Statement(trenche, SUPPORTS, treatment)
  if __debug__:
    print s
  M.add_statement(s)


def get_treatment_from_label(label):
  return [
    t['treatment'] for t in _query("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cd: <http://choicedocs.com/ref/>
SELECT distinct ?treatment
WHERE {
    ?treatment rdf:type cd:Treatment .
    ?treatment rdfs:label "%(label)s" .
}
""",
  label=label,
  )]


def get_trenche_from_label(label):
  return [
    t['trenche'] for t in _query("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cd: <http://choicedocs.com/ref/>
SELECT distinct ?trenche
WHERE {
    ?trenche rdf:type cd:Trenche .
    ?trenche rdfs:label "%(label)s" .
}
""",
  label=label,
  )]


def get_trenche_support():
  return _query("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cd: <http://choicedocs.com/ref/>
SELECT distinct ?tlabel ?ttname
WHERE {
    ?t rdfs:label ?tlabel .
    ?tt cd:name ?ttname .
    ?t cd:SupportsTreatment ?tt .
}
""")




##add_treatment("Acupuncture", "Acupuncture is Fun")
##add_treatment_to_trenche("Acupuncture is Fun", "A")
##
##q = get_trenche_support()
##
##print
##print "%(tlabel)s supports %(ttname)s" % q[0]
##print



















