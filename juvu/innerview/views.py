from django.template import RequestContext
from django.shortcuts import render_to_response
from juvu.innerview.models import get_model, simple_query

DEFAULT_QUERY = '''\
SELECT distinct ?spa ?time ?tname ?price
WHERE {
  ?pt foaf:name "Womens Cut" .
  ?pt rdf:type cd:ProcedureType .
  ?t cd:SubCategory ?pt .
  ?t rdf:type cd:Treatment .
  ?t foaf:name ?tname .
  ?a cd:Treatment ?t .
  ?a cd:Date "03-05-2012" .
  ?a cd:Provider ?spa .
  ?a cd:from_time ?time .
  ?a cd:Price ?price .
}
'''

def _proc_URI(uri):
    try:
        return str(uri)
    except:
        return str(uri.uri)

def _proc_result(r):
    return str(dict(
        (k, _proc_URI(v))
        for k, v in r.iteritems()
        ))

def home(request):
    '''
    
    '''
    if  request.method != 'POST':
        results = None
        query = DEFAULT_QUERY
    else:
        prefix_text = request.POST['prefix_text']
        query = request.POST['query_text']
        print repr(query), query
        query_type = request.POST.get('query_type', 'SPARQL')

        m = get_model()
        Q = simple_query(m, query, prefix_text)
##        print Q
        results = '\n'.join(_proc_result(result) for result in Q)

    return render_to_response(
            'innerview.html',
            {
                'results': results or 'No results',
                'query': query,
                },
            context_instance=RequestContext(request),
            )
