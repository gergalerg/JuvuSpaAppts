from RDF import Uri


OUR_LAND = 'http://choicedocs.com/ref/'
OUR_LAND_URI = Uri(OUR_LAND)

NAME = Uri(OUR_LAND + 'name')
PROVIDER = Uri(OUR_LAND + 'Provider')
TRENCHE = Uri(OUR_LAND + 'Trenche')
TREATMENT = Uri(OUR_LAND + 'Treatment')
SUPPORTS = Uri(OUR_LAND + 'SupportsTreatment')

LABEL = Uri('http://www.w3.org/2000/01/rdf-schema#label')
TYPE = Uri('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')

PREFIX = """\
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cd: <http://choicedocs.com/ref/>
"""
