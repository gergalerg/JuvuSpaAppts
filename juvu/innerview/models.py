from django.conf import settings
from RDF import (
    Storage,
    Model,
    Statement,
    Node,
    SPARQLQuery,
)


_M = None
def get_model():
    global _M
    if not _M:
        _M = Model(Storage(**settings.TRIPLE_STORES['testdata']))
    return _M

