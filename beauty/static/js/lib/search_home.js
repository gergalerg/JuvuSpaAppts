
//-------------------------------------------------------
// Miscellaneous functions.
//

function toc_in() {
    $("#toc").fadeOut(150, 'easeOutBounce', function() {
        $("#main_frame").fadeIn();
    });
}

function toc_out() {
    $("#main_frame").fadeOut(150, function() {
        $("#toc").fadeIn(150);
    });
}

function setup_button(sel, ico) {
    $(sel).button({icons: {primary:ico}, text: false })
        .click(function(){return false});
}

function params_into_object(d, initial) {
    _.each(d, function(foo) {
        initial[foo.name] = foo.value;
    });
}

function show_tree() {
    var upper = duration / 1.16;

    $("#toc_inner").hide("blind", upper, function() {
        $("#goey").fadeIn();
        $("#login_head").fadeIn();
    });

    tree_node_click(root);

    var s = d3.select("#tree").select("svg")
    s.transition()
    .ease("linear")
    .duration(duration)
    .attr("height", w + m[1] + m[3])
    ;

    s.selectAll("g.treebox")
    .transition()
    .ease("linear")
    .duration(duration / 1.8193)
    .attr("transform", "translate(120,10)");
    ;

    s.selectAll("g.node").on("click", tree_node_click);

    s.selectAll("text")
    .transition()
    .duration(duration)
    .style("fill-opacity", 1)
    .attr("font-weight", 100)
    .attr("fill", 'black')
    .attr("font-size", 16)
    ;

}

function hide_tree() {
    var s = d3.select("#tree").select("svg")
    s.transition()
    .attr("height", 150)
    ;
    collapse(root);
    update(root);
    s.selectAll("g.treebox")
    .transition()
    .attr("transform", function(d) { return "translate(240,-300)" })
    ;
    _.delay(change_me_node, 200);

    $("#goey").fadeOut(function() {
        $("#toc_inner").show("blind");
    });

    s.selectAll("text")
    .transition()
    .duration(0)
    .attr("font-size", 28)
    .attr("font-weight", 400)
    .attr("fill", '#2A85E8')
    .style("fill-opacity", 1)
    ;
}

function change_me_node() {
    var s = d3.select("#tree").select("svg")
    var node = s.selectAll("g.node")

    node.selectAll("circle")
    .transition()
    .duration(0)
    .attr("r", 0)
    ;

    node.on("click", show_tree);
}

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
    }

    if (_.isUndefined(options.nickname)) {
        this.nickname = ko.observable(options.name);
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
        return "$" + (+this.price()).toFixed(2);
    }, this);

    this.toggle = function() {
        this.supported(!this.supported());
    }

    this.make_current = function() {
        viewModel.current_proc(this);
    }
}


//-------------------------------------------------------
// View Model
//

var viewModel = {

    // Track the current "view" the user is looking at.
    viewing: ko.observable(),

    // Track which time display mode user is using (month, week, year, etc...)
    time_mode: ko.observable('year'),

    // Displayed criteria/options.
    criteria_mode: ko.observable(),

    // The currently selected treatment ("proc"edure), if any.
    current_proc: ko.observable({name:'None Selected'}),

    current: ko.observable(""),
    current_el: ko.observable(),

    pointed_at: ko.observable("Wants Pawn Term, "),
    pointed_at_el: ko.observable(),

	is_current: function(d) {
	    return viewModel.current() == d.label;
	},
};


//-------------------------------------------------------
// View
//

var View = {
    // This is the last view the user was looking at, used for determining
    // correct transition to a new view.
    previous_view: "toc",

    previous: false,
    pointed_at: false,
};

viewModel.time_mode.subscribe(function(tmode) {
    console.log("Time mode:", tmode);
    if (tmode != 'year') {
        month_tabs_fade(vis3);
    }

    switch (tmode[0]) {
        case 'y': // switch to year.
            select_year();
            month_tabs_unfade(vis3)
            break;
        case 'm': // switch to month.
            select_month(tmode.substr(1));
            break;
        case 's': // switch to selection.
            select_dates()
            break;
    }
});

/*
viewModel.viewing.subscribe(function(view) {
    if (view == "year") {
        select_year();
    } else if (view[0] == 'w') {
        select_week(view.slice(1));
    } else if (view[0] == 'd') {
        select_day(view.slice(1));
    } else {
        select_month(view);
    }
});
*/


// Track and update visible pane and TOC width.  This links viewModel.viewing
// and View.previous_view.
viewModel.viewing.subscribe(function(view) {

    console.log("Track and update visible pane and TOC width =>", view);

    // I think this is prevented by the routes thingy, but it can't hurt.
    if (view == View.previous_view) { return };

    // Are we going to the TOC?
    if (view == "toc") {
        toc_out(); // The rest of the UI remains static,
    } else if (view == "tree") {
        // hide login and sign up

        // expand tree and morph name/"me"

    // No, we're going to one of the panes.
    } else {
        // Clear the previous view.
        if (View.previous_view == "toc") {
            toc_in();
            $(".current_pane").hide().removeClass("current_pane");
            $("#pane_" + view).show().addClass("current_pane");
        } else  if (view == "1" && View.previous_view && View.previous_view[0] == 'm') {
            // month to year view switch
            select_year();
        } else {
            switch_pane(view);
        }
    };

    // Update history for next call.
    View.previous_view = view;
});

function switch_pane(pane) {
    $(".current_pane").hide("fade", 175, function() {
        $("#pane_" + pane).show("fade", 175).addClass("current_pane");
    }).removeClass("current_pane");
}


viewModel.viewing.subscribe(function(view) {
    $(".indicate").removeClass("indicate");
    $("#" + view + "_link").addClass("indicate");
});

viewModel.pointed_at_el.subscribe(function(it) {
    if (it) {
        it = d3.select(it);
        //it.transition().call(embiggen);
    } else if (View.pointed_at) {
        // Don't shrink current day.
        View.pointed_at.filter(function(d) {
            return !viewModel.is_current(d);
        })
        //.transition().call(shrink);
    }
    View.pointed_at = it;
});

viewModel.current_el.subscribe(function(it) {
    var circ = d3.select(it);
    circ.transition().call(swell);
    if (View.previous) {
        View.previous.transition()
        //.call(shrink)
        .attr("fill-opacity", 0.5);
    }
    View.previous = circ;
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
            this.navigate("toc", true);
        }
    },

});

var routes = new routey();

//-------------------------------------------------------
// Tree Layout Junk.
//

var m = [10, 120, 10, 120],
    w = 714 - m[1] - m[3],
    h = 400 - m[0] - m[2],
    i = 0,
    duration = 500;

var tree = d3.layout.tree()
    .size([700, w]);

var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.y, d.x]; });

// Toggle tree children on click.
function tree_node_click(d) {
  if (!_.has(d, "children")) {
    d.supported(!d.supported());
  } else if (d.children) {
    d._children = d.children;
    d.children = null;
  } else {
    d.children = d._children;
    d._children = null;
  }
  update(d);
}

function collapse(d) {
    if (d.children) {
      d._children = d.children;
      _.each(d._children, collapse);
      d.children = null;
    }
}

var vis2;
var vis3;

function update(source) {

  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse();

  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 110; });

  // Update the nodes…
  var node = vis2.selectAll("g.node")
      .data(nodes, function(d) { return d.id || (d.id = ++i); });

  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("svg:g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
      .on("click", tree_node_click);

  nodeEnter.append("svg:circle")
      .attr("r", 1e-6);

  nodeEnter.append("svg:text")
      .attr("x", function(d) { return d.children || d._children ? -10 : 10; })
      .attr("dy", ".35em")
      .attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
      .text(function(d) { return d.name; })
      .attr("fill", 'black')
      .attr("font-size", 16)
      .style("fill-opacity", 1e-6);

  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
      .duration(duration)
      .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

  nodeUpdate.select("circle")
      .attr("r", 8)
      .style("fill", function(d) {
          if (d.children || _.has(d, "supported") && d.supported()) {
              return "lightsteelblue";
          }
          return "#eef";
      });

  nodeUpdate.select("text")
      .style("fill-opacity", 1);

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node.exit().transition()
      .duration(duration)
      .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
      .remove();

  nodeExit.select("circle")
      .attr("r", 1e-6);

  nodeExit.select("text")
      .style("fill-opacity", 1e-6);

  // Update the links…
  var link = vis2.selectAll("path.link")
      .data(tree.links(nodes), function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("svg:path", "g")
      .attr("class", "link")
      .attr("d", function(d) {
        var o = {x: source.x0, y: source.y0};
        return diagonal({source: o, target: o});
      })
    .transition()
      .duration(duration)
      .attr("d", diagonal);

  // Transition links to their new position.
  link.transition()
      .duration(duration)
      .attr("d", diagonal);

  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
      .duration(duration)
      .attr("d", function(d) {
        var o = {x: source.x, y: source.y};
        return diagonal({source: o, target: o});
      })
      .remove();

  // Stash the old positions for transition.
  nodes.forEach(function(d) {
    d.x0 = d.x;
    d.y0 = d.y;
  });
}


//-------------------------------------------------------
// Teh Year Data.
//

var year = d3.time.days(new Date(2012, 0, 1), new Date(2013, 0, 1));
var data = jQuery.map(year, function(d, i) {
    var datum = {
        "month": month(d),
        "week_of_year": +week(d),
        "day_of_week": day(d),
        "day_of_month": mday(d),
        "day_of_year": +yday(d),
        "label": format(d),
        "date": d,
    };
    var months_week = week(new Date(2012, datum.month, 1));
    datum.week_of_month = datum.week_of_year - months_week;
    return datum;
});

//-------------------------------------------------------
// Mouse bindings for the day-circles.
// Mostly to de-couple the viewModel logic from the d3 transitions that
// animate it.

function mouse_bindings(T) { T
	.on("mouseover", function(d) {
        viewModel.pointed_at(d.label);
        viewModel.pointed_at_el(this);
    })
	.on("mouseout", function(d) {
        var c = viewModel.current();
        viewModel.pointed_at((c != "") ? c : "Select Date");
        viewModel.pointed_at_el(false);
    })
	.on("click", function(d) {
        if (!viewModel.is_current(d)) {
            viewModel.current(d.label);
            viewModel.current_el(this);
            routes.navigate("day/" + d.day_of_year, true);
        }
    });
}

//-------------------------------------------------------
// Mouse bindings for the Month Tabs.
// Mostly to de-couple the viewModel logic from the d3 transitions that
// animate it.

function month_mouse_bindings(T) { T
	.on("mouseover", function(d) {
	    console.log(this);
/*    })
	.on("mouseout", function(d) {
        var c = viewModel.current();
        viewModel.pointed_at((c != "") ? c : "Select Date");
        viewModel.pointed_at_el(false);
    })
	.on("click", function(d) {
        if (!viewModel.is_current(d)) {
            viewModel.current(d.label);
            viewModel.current_el(this);
            routes.navigate("day/" + d.day_of_year, true);
        }
*/    });
}


//-------------------------------------------------------
// Initial bootstrap.
//


function select_dates() {
    var from_date = $("#from_date_cal").datepicker("getDate");
    var to_date = $("#to_date_cal").datepicker("getDate");
    if (!(_.isNull(from_date) || _.isNull(to_date))) {
        select_date_range(from_date, to_date);
        $("#options_criteria").fadeIn(CriteriaControls.show_options);
    }
}

function select_today() {
    $("#from_date_cal").datepicker("setDate", "+0")
    $("#to_date_cal").datepicker("setDate", "+0")
    if (viewModel.time_mode() != 'selection') {
        viewModel.time_mode('selection');
    } else {
        select_dates();
    }
}

function date_selected() {
    CriteriaControls.hide_where();
    $("#distance_criteria > h3").fadeOut();
    if (viewModel.time_mode() != 'selection') {
        viewModel.time_mode('selection');
    } else {
        select_dates();
    }
}



function show_it(first, second) {
    $(first).animate({
        opacity: 1,
        fontSize: '35px',
        },
        function () { $(second).fadeIn() }
     );
}

function hide_it(first, second, third) {
    $(first).fadeOut(function () {
        $(second).fadeOut(function () {
            $(third).animate({
              opacity: .5,
              fontSize: '150%',
            });
        });
    });
}




var CriteriaControls = {
    show_where: function () { show_it("#where", "#where_criteria > h3") },
    hide_where: function () { hide_it("#miles_criteria", "#where_criteria > h3", "#where") },

    show_when: function () { $("#when_criteria").fadeIn(); },
    hide_when: function () { hide_it("#date_criteria", "#when_criteria > h3", "#when") },

    show_options: function () { show_it("#options", "#options_interior") },
    hide_options: function () { hide_it("#amenities", "#options_interior", "#options") },

    show_miles: function () { $("#miles_criteria").fadeIn(); },
    hide_miles: function () { $("#miles_criteria").fadeOut(); },

    show_date_range: function () { $("#date_criteria").fadeIn(); },
    hide_date_range: function () { $("#date_criteria").fadeOut(); },

    show_distance: function () { $("#distance_criteria > h3").fadeIn(); },
    hide_distance: function () { $("#distance_criteria > h3").fadeOut(); },

    show_price: function () {
        $("#price_options").toggle("slide");
        $("#price_header").toggleClass("elbowroom");
        
    },
    show_discount: function () {
        $("#discount_options").toggle("slide");
        $("#discount_header").toggleClass("elbowroom");
    },
    show_meplus: function () {
        $("#meplus_options").toggle("slide");
        $("#meplus_header").toggleClass("elbowroom");
    },

    toggle_amenities: function () {
        $("#amenities").toggle("fold");
    },
}



