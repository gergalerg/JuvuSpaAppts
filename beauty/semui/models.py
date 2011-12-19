from RDF import (
    Storage,
    Model,
    Statement,
    Node,
    Uri,
    SPARQLQuery,
    RDFXMLSerializer,
)
from spasui.models import (
    M,
    add_provider,
    add_staff_member,
    plain_query,
    )
from beauty.util.URIs import (
    OUR_LAND,
    NAME,
    PROVIDER,
    TRENCHE,
    TREATMENT,
    SUPPORTS,
    LABEL,
    TYPE,
    AVAIL,
    DATE,
#    PREFIX,
    WHERE,
    FROM_TIME,
    TO_TIME,
    EMPLOYS,
    )


PREFIX = {
# Included by default. #    'rdf': '<http://www.w3.org/1999/02/22-rdf-syntax-ns#>',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'foaf': 'http://xmlns.com/foaf/0.1/',
    'cd': 'http://choicedocs.com/ref/',
    }


S = RDFXMLSerializer()
for k, v in PREFIX.iteritems():
    S.set_namespace(k, v)

##print S.serialize_model_to_string(M)
##print; print; print
##
##
add_provider("Larry's Spa", "Larry")
add_staff_member("Larry", "Barry")


@plain_query
def get_staff_member(spa, staff_tag):
  """
  SELECT distinct ?staffmember
  WHERE {
      ?staffmember rdfs:label "%(staff_tag)s" .
      ?spa rdfs:label "%(spa)s" .
      ?spa cd:Employs ?staffmember .
  }
  """


def GET_staff_member(spa, staff_tag):
    q = get_staff_member(spa, staff_tag)
    assert q, repr(q)
    staffmember = q[0]['staffmember']
    s = Statement(subject=staffmember)
    stream = M.find_statements(s)
    m = Model()
    m.add_statements(stream)
    xml = S.serialize_model_to_string(m)
##    xml = S.serialize_model_to_string(M)
    return xml

##print S.serialize_model_to_string(M)
##print; print; print

