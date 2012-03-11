function random_apts(staff_member) {
    var res = [Math.random(), Math.random(), Math.random(), Math.random(), Math.random(), Math.random()];
    res.sort();
    res = _.map(res, day_to_n.invert);
    return [
        { start: res[0], end: res[1], staff_member: staff_member },
        { start: res[2], end: res[3], staff_member: staff_member },
        { start: res[4], end: res[5], staff_member: staff_member }
    ];
}


//-------------------------------------------------------
// Staff member calendar view support.
//

var color_of = d3.scale.linear()
        .domain([0, 1])
        .range(["hsl(0, 50%, 70%)", "hsl(360, 50%, 70%)"])
        .interpolate(d3.interpolateHsl);

function setup_bands() {
    var R = _.range(viewModel.staff().length);
    var x = d3.scale.ordinal()
        .domain(R)
        .rangeBands([80, 335], 0.125);
    var col = d3.scale.ordinal()
        .domain(R)
        .rangePoints([0.0, 1.0], 0.5);

    _.each(viewModel.staff(), function(n, i) {
        n.tag_color(color_of(col(i)));
    });

    var Apointments = _.flatten(_.map(viewModel.staff(), random_apts));

    d3.select("svg")
      .selectAll("rect")
      .remove();

    d3.select("svg")
      .selectAll("rect")
      .data(Apointments)
      .enter().append("svg:rect")
        .attr("x", function(d) { return x(_.indexOf(viewModel.staff(), d.staff_member)) })
        .attr("width", x.rangeBand())
        .attr("y", function(d) { return day_line(d.start) })
        .attr("height", function(d) { return day_line(d.end) - day_line(d.start) })
        .attr("fill", function(d) { return d.staff_member.tag_color() })
        .on("mouseover", function(d) {
            viewModel.mouse_time(hour(d.start));
        });

}


//-------------------------------------------------------
// Miscellaneous functions.
//

function toc_in() {
    $("#toc").switchClass("seven", "two", 500, 'easeOutBounce', function() {
        $("#main_frame").fadeIn();
    });
}

function toc_out() {
    $("#main_frame").fadeOut(150, function() {
        $("#toc").switchClass("two", "seven", 150);
    });
}

function setup_button(sel, ico, show_text) {
    show_text = show_text || false;
    $(sel).button({icons: {secondary:ico}, text: show_text })
        .click(function(){return false});
}

function params_into_object(d, initial) {
    _.each(d, function(foo) {
        initial[foo.name] = foo.value;
    });
}

function toggle_resources() {
    $("#resource_picker_inner").toggle("blind");
};

function toggle_staff_classs() {
    $("#staff_class_picker_inner").toggle("blind");
};

function toggle_addon_procs() {
    $("#addon_procs_picker_inner").toggle("blind");
};

function toggle_options_procs() {
    $("#addon_options_picker_inner").toggle("blind");
};


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

//-------------------------------------------------------
// View Model Classes
//

var SpaProcedure = function(options) {
    this.name = options.name;
    this.supported = ko.observable(options.supported);

    if (!_.isUndefined(options.children)) {
        this.children = _.map(
            options.children,
            function(n) { return new SpaProcedure(n) }
        );
    } else {
        this.children = null;
    }

    if (_.isUndefined(options.nickname)) {
        this.nickname = ko.observable("");
    } else {
        this.nickname = ko.observable(options.nickname);
    }

    if (_.isUndefined(options.price)) {
        this.price = ko.observable(0.0);
    } else {
        this.price = ko.observable(options.price);
    }

    if (_.isUndefined(options.duration)) {
        this.duration = ko.observable(60);
    } else {
        this.duration = ko.observable(options.duration);
    }

    this.formatted_price = ko.dependentObservable(function() {
        return "$" + (+this.price()).toFixed(0);
    }, this);

    this.toggle = function() {
        this.supported(!this.supported());
        this.make_current();
    }

    this.make_current = function() {
        viewModel.current_proc(this);
    }

    if (_.isUndefined(options.subtypes)) {
        this.subtypes = ko.observableArray([]);
    } else {
        this.subtypes = options.subtypes;
    }

    this.add_subtype = function() {
        var new_subtype = $("form#add_subtype").serializeArray();
        var n = {name: this.name, supported:true, subtypes:this.subtypes};
        params_into_object(new_subtype, n);
        console.log(n);
        var newb = new SpaProcedure(n);
        this.subtypes.push(newb);
        viewModel.supported_procs.push(newb);
        this.nickname("");
    }
}

var StaffMember = function(options) {
    this.name = options.name;
    this.tag_color = ko.observable('#fff');
    this.staff_classes = ko.observableArray([]);

    this.remove = function() {
        viewModel.stuffs.remove(this);
        if (viewModel.stuffs().length == 0 || viewModel.current_staff_member() == this) {
            viewModel.current_staff_member({});
        }
    }

    this.make_current = function() {
        viewModel.current_staff_member(this);
    }

}


//-------------------------------------------------------
// Static Data
//


// Convert the (server-embedded) JSON to KO models.
root.children = _.map(root.children, function(n) { return new SpaProcedure(n); });

staff = _.map(staff, function(n) { return new StaffMember(n); });


//-------------------------------------------------------
// View Model
//

viewModel = {

    // Track the current "view" the user is looking at.
    viewing: ko.observable(),

    // The currently selected treatment ("proc"edure), if any.
    current_proc: ko.observable({name:'None Selected', subtypes:[]}),

    // Array of SpaProcedure objects that a spa supports.
    supported_procs: ko.observableArray(),

    // The master tree of spa procedures.
    obj_treatments: ko.observableArray(root.children),

    // Staff members, and currently selected staff member.
    staff: ko.observableArray(staff),
    current_staff_member: ko.observable({"staff_classes":ko.observableArray()}),

    staff_classes: ko.observableArray([{name:'but'}, {name:'sects'}]),
    current_staff_class: ko.observable({name:''}),
    staff_with_class: ko.observableArray(staff),
    current_staff_member_staff_classes: ko.observableArray([]),

    // Display the time corresponding to the mouse position on the calendar pane.
    mouse_time: ko.observableArray(),

    // A bit of indirection to allow binding to this callback before current_proc is specified.
    add_subtype: function () {
        viewModel.current_proc().add_subtype();
    },

    add_staff_member: function() {
        var name = $("#staff_name").val();
        if (name != "") {
            var newbie = new StaffMember({
                name: name,
                description: 'Bananas and Peanutbutter',
                extraCost: 0.25,
            })
            this.staff.push(newbie);
            this.current_staff_member(newbie);
            $("#staff_name").val('');
            setup_bands();
        } else {
            $("#staff_name").effect('highlight');
        }
    },

    add_class: function() {
        var new_class = $("#id_add_class").val();
        if (!new_class) { return }
        viewModel.staff_classes.push({name:new_class});
        $("#id_add_class").val("");
    },
};

viewModel.someone_selected = ko.dependentObservable(function() {
    return !_.isEmpty(this.current_staff_member());
}, viewModel);

viewModel.view_title = ko.dependentObservable(function() {
    var lookup = {
        'toc': 'Home',
        0: 'Info',
        1: 'Services',
        2: 'Customize',
        3: 'Staff',
        4: 'Calendar',
    };
    console.log(this.viewing());
    return lookup[this.viewing()];
}, viewModel);

//-------------------------------------------------------
// View
//

var View = {
    // This is the last view the user was looking at, used for determining correct transition to a new view.
    previous_view: "toc",

};

function display_staff_members_staff_classes(classes) {
    var d = $("#put_it_here");
    d.empty();
    _.map(classes, function(staff_class) {

        var m = d.append('  <div style="margin-bottom: 9px;">'
               + staff_class.name
               + '    <button class="expando_staff_class">Expand</button>'
               + '    <button class="del_staff_class">Delete</button>'
               + '  </div>');

        m.find(".expando_staff_class").button({
            icons: {secondary:'ui-icon-circle-triangle-s'},
            text: false,
        })
        .click(function(){return false});

        m.find(".del_staff_class").button({
            icons: {secondary:'ui-icon-circle-close'},
            text: false,
        })
        .click(function(){return false});

    });
}

// 
viewModel.current_staff_member.subscribe(function(staff_member) {
    var classes = staff_member.staff_classes();
    display_staff_members_staff_classes(classes);
    $("#current_staff_member_staff_class").val("");
});

// Update the "indicate" CSS class.
viewModel.viewing.subscribe(function(view) {
    $(".indicate").removeClass("indicate");
    $("#" + view + "_link").addClass("indicate");
});

// Track and update visible pane and TOC width.
viewModel.viewing.subscribe(function(view) {

    // I think this is prevented by the routes thingy, but it can't hurt.
    if (view == View.previous_view) { return };

    // Are we going to the TOC?
    if (view == "toc") {
        toc_out(); // The rest of the UI remains static,

    // No, we're going to one of the panes.
    } else {
        // Clear the previous view.
        if (View.previous_view == "toc") {
            toc_in();
            $(".current_pane").hide().removeClass("current_pane");
            $("#pane_" + view).show().addClass("current_pane");
        } else {
            $(".current_pane").hide("fade", 175, function() {
                $("#pane_" + view).show("fade", 175).addClass("current_pane");
            }).removeClass("current_pane");
        }
    };

    // Update history for next call.
    View.previous_view = view;
});

//-------------------------------------------------------
// Route URLs.
//

var routey = Backbone.Router.extend({

    routes: {
        "toc": "toc",
        "step/:num": "step",
    },

    toc: function() {
        viewModel.viewing("toc");
    },

    step: function(num) {
        num = +num;
        if (num >= 0 && num <= 4) {
            viewModel.viewing(num);
        } else {
            routes.navigate("toc", true);
        }
    },

});

var routes = new routey();

