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
var FOAF_NAME = $.rdf.resource('foaf:name', {namespaces: RDF_NS});
var PROC_TYPE = $.rdf.resource('cd:ProcedureType', {namespaces: RDF_NS});
var TREATMENT_TYPE = $.rdf.resource('cd:Treatment', {namespaces: RDF_NS});
var SUB_CAT = $.rdf.resource('cd:SubCategory', {namespaces: RDF_NS});


function gather() {
    var tripstore = new_triplestore();
    function add(s, p, o) {
        tripstore.add($.rdf.triple(s, p, o, {namespaces: RDF_NS}));
    }
    _.each(viewModel.supported_procs(), function(proc) {
        var pt = proc.get_RDF_node(tripstore);

        var subtype_node = $.rdf.blank('[]');
        var subtype_name = $.rdf.literal('"' + proc.nickname + '"');

        add(subtype_node, FOAF_NAME, subtype_name);
        add(subtype_node, $.rdf.type, TREATMENT_TYPE);
        add(subtype_node, SUB_CAT, pt);
//        add();
    });
    return tripstore;
}


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

