from RDF import (
    Storage,
    Model,
    Statement,
    Node,
    Uri,
    Parser,
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
    PREFIX,
    WHERE,
    FROM_TIME,
    TO_TIME,
    EMPLOYS,
    )


PREFIXd = {
# Included by default. #    'rdf': '<http://www.w3.org/1999/02/22-rdf-syntax-ns#>',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'foaf': 'http://xmlns.com/foaf/0.1/',
    'cd': 'http://choicedocs.com/ref/',
    }


S = RDFXMLSerializer()
for k, v in PREFIXd.iteritems():
    S.set_namespace(k, v)


def serialize_stream(stream):
    m = Model()
    m.add_statements(stream)
    return S.serialize_model_to_string(m)

##print S.serialize_model_to_string(M)
##print; print; print
##
##
add_provider("Larry's Spa", "Larry")
add_staff_member("Larry", "Barry")
add_staff_member("Larry", "Carrie")
add_staff_member("Larry", "Gary")


def expect(*fields):
    def deco(f):
        def wrapper(*a, **b):
            q = f(*a, **b)
            q = [
                dict((k, res[k]) for k in fields)
                for res in q
                ]
            return q
        return wrapper
    return deco


def expect_one(*fields):
    def deco(f):
        def wrapper(*a, **b):
            q = f(*a, **b)
            q = q[0]
            q = dict((k, q[k]) for k in fields)
            return q
        return wrapper
    return deco


@expect_one('staffmember')
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


def get_staff(spa):
    sparql = PREFIX + """
    CONSTRUCT { ?staffmember rdfs:label ?name }
    WHERE {
      ?spa rdfs:label "%(spa)s" .
      ?spa cd:Employs ?staffmember .
      ?staffmember rdfs:label ?name.
    }
    """ % {'spa':str(spa)}
    query = SPARQLQuery(sparql)
##    import pdb; pdb.set_trace()
    res = query.execute(M)
    return res

def GET_staff(spa):
    q = get_staff(spa)
    stream = q.as_stream()
    xml = serialize_stream(stream)
    return xml

def GET_staff_member(spa, staff_tag):
    q = get_staff_member(spa, staff_tag)
    s = Statement(subject=q['staffmember'])
    stream = M.find_statements(s)
    xml = serialize_stream(stream)
##    xml = S.serialize_model_to_string(M)
    return xml

##print S.serialize_model_to_string(M)
##print; print; print

def POST_staff(spa, rdf):
    parser = Parser(mime_type="application/rdf+xml")
    for statement in parser.parse_string_as_stream(rdf, OUR_LAND):
        print statement
    return rdf, 'staff_member_name'




