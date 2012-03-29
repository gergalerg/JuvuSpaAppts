from RDF import (
    Storage,
    Model,
    Statement,
    Node,
    SPARQLQuery,
)
from django.conf import settings
from juvu.util.URIs import (
  PREFIX,
  )


_M = None
def get_model():
    global _M
    if not _M:
        _M = Model(Storage(**settings.TRIPLE_STORES['testdata']))
    return _M


def simple_query(m, sparql, prefix=PREFIX):
  sparql = str(prefix + sparql)
  print sparql
  return SPARQLQuery(sparql).execute(m)
