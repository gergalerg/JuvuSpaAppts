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
LABEL = Uri('http://www.w3.org/2000/01/rdf-schema#label')
TYPE = Uri('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')


M = Model(Storage(**settings.TRIPLE_STORES['default']))


def provider_named(name):
  q = SPARQLQuery("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cd: <http://choicedocs.com/ref/>
SELECT distinct ?a
WHERE {
    ?a rdf:type cd:Provider .
    ?a cd:name "%(name)s" .
}
  """ % {'name': name})
  return list(q.execute(M))


def add_provider(name, label):
  # Begin transaction
  provider = Node()
  f = lambda p, o: Statement(provider, p, o)
  for s in (
    f(TYPE, PROVIDER),
    f(NAME, name),
    f(LABEL, label),
    ):
    M.add_statement(s)
  return provider
