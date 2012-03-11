//-------------------------------------------------------
// RDF Processing.
//

var RDF_NS = { 
    rdf: 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    rdfs: 'http://www.w3.org/2000/01/rdf-schema#',
    dc: 'http://purl.org/dc/elements/1.1/', 
    foaf: 'http://xmlns.com/foaf/0.1/'
    };

function new_triplestore() {
    return $.rdf.databank([],
    {
        base: 'http://choicedocs.com/ref/',
        namespaces: RDF_NS,
    }
)};

var TRIPLESTORE = new_triplestore();

TRIPLESTORE.add('_:creator a foaf:Person')
TRIPLESTORE.add('_:creator foaf:name "Bill"')

var Q = $.rdf({databank: TRIPLESTORE})
    .where('?person a foaf:Person')
    .where('?person foaf:name ?name')
    .each(function() {
        console.log(this.person.value, this.name.value);
    });


function post_new_staff_member(who) {
    var trip = new_triplestore();
    trip.add('_:newb rdfs:label "' + who + '"');
    var payload = trip.dump({format:'application/rdf+xml'})
    $.ajax({
        url: "{% url staff 'Larry' %}",
        type: 'POST',
        contentType: 'application/rdf+xml',
        data: payload,
        processData: false,
        success: function(data, textStatus, jqXHR) {
            console.log(data);
            var K = new_triplestore();
            K.load(data);
            console.log(K.dump());
        },
    });
}

