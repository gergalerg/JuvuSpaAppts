
//-------------------------------------------------------
// View Model
//

var SpaProcedure = function(options) {
    this.name = options.name;
    this.nickname = ko.observable(options.name);
    this.supported = ko.observable(options.supported);

    if (!_.isUndefined(options.children)) {
        this.children = _.map(
            options.children,
            function(n) { return new SpaProcedure(n) }
        );
    }

    this.price = ko.observable(0.0);
    this.duration = ko.observable(60);

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

var StaffMember = function(options) {
    this.name = options.name;
    this.description = options.description;
    this.extraCost = options.extraCost;

    this.remove = function() {
        viewModel.stuffs.remove(this);
        if (viewModel.stuffs().length == 0 || viewModel.current() == this) {
            viewModel.current({});
        }
    }

    this.make_current = function() {
        viewModel.current(this);
    }
}

// Convert the (server-embedded) JSON to KO models.
root.children = _.map(root.children, function(n) { return new SpaProcedure(n); });

var availableMeals = _.map([
        { name: 'Billy', description: 'Dry crusts of bread', extraCost: 0 },
        { name: 'Bob', description: 'Fresh bread with cheese', extraCost: 9.95 },
        { name: 'Billy Jo Bob', description: 'Caviar and vintage Dr Pepper', extraCost: 18.50 },
    ],
    function(n, i){ return new StaffMember(n) });

var viewModel = {
    viewing: ko.observable(),
    stuffs: ko.observableArray(availableMeals),
    current: ko.observable(availableMeals[0]),

    obj_treatments: ko.observableArray(root.children),

    current_proc: ko.observable({name:'None Selected'}),

    add_staff_member: function() {
        var name = $("#staff_name").val();
        if (name != "") {
            var newbie = new StaffMember({
                name: name,
                description: 'Bananas and Peanutbutter',
                extraCost: 0.25,
            })
            this.stuffs.push(newbie);
            this.current(newbie);
            $("#staff_name").val('');
        } else {
            $("#staff_name").effect('highlight');
        }
    },
};

viewModel.display_view_name = ko.dependentObservable(function() {
    var viewing = this.viewing();
    return (viewing == 'dash') ? '' : viewing + 1;
}, viewModel);

//-------------------------------------------------------
// View
//

var View = {
    previous_view: 0,
};

viewModel.viewing.subscribe(function(view) {
    $(".indicate").removeClass("indicate");
    $("#" + view + "_link").addClass("indicate");
});

viewModel.viewing.subscribe(_.throttle(function(view) {
    var i = (view == "dash") ? 4 : +view;
    var delta = i - View.previous_view;
    if (!delta) {
        return;
    }
    var leaving = delta < 0 ? 'right' : 'left';
    var arriving = delta < 0 ? 'left' : 'right';
    var panes = $(".pane");

    function f(target, previous, leaving, arriving) {
        if (target == previous) { return };
        var next = previous - (target < previous ? 1 : -1);
        $(panes[previous]).hide("slide", { direction: leaving, }, 150, function() {
            $(panes[next]).show("slide", { direction: arriving }, 150, function() {
                f(target, next, leaving, arriving);
            });
        });
    }
    f(i, View.previous_view, leaving, arriving);
    View.previous_view = i;
},
1000));

//-------------------------------------------------------
// Route URLs.
//

var routey = Backbone.Router.extend({

    routes: {
        "d": "dash",
        "step/:num": "step",
    },

    dash: function() {
        viewModel.viewing("dash");
    },

    step: function(num) {
        num = +num;
        if (num >= 0 && num < 4) {
            viewModel.viewing(num);
        } else {
            routes.navigate("step/0", true);
        }
    },

});

var routes = new routey();

//-------------------------------------------------------
// Tree Layout Junk.
//

var m = [10, 120, 10, 120],
    w = 914 - m[1] - m[3],
    h = 800 - m[0] - m[2],
    i = 0,
    duration = 500;

var tree = d3.layout.tree()
    .size([h, w]);

var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.y, d.x]; });

// Toggle tree children on click.
function tree_node_click(d) {
  if (d.children) {
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

var vis;

function update(source) {

  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse();

  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 110; });

  // Update the nodes…
  var node = vis.selectAll("g.node")
      .data(nodes, function(d) { return d.id || (d.id = ++i); });

  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("svg:g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
      .on("click", tree_node_click);

  nodeEnter.append("svg:circle")
      .attr("r", 1e-6)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#eef"; });

  nodeEnter.append("svg:text")
      .attr("x", function(d) { return d.children || d._children ? -10 : 10; })
      .attr("dy", ".35em")
      .attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
      .text(function(d) { return d.name; })
//      .style("fill", function(d) { return (d.supported && d.supported()) ? "black" : "#ccc"; })
      .style("fill-opacity", 1e-6);

  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
      .duration(duration)
      .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

  nodeUpdate.select("circle")
      .attr("r", 8)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#eef"; });

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
  var link = vis.selectAll("path.link")
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
// Fire 'er up!
//

$(function(){

    $(".pane").hide();
    $("#pane_0").show();

    ko.applyBindings(viewModel);

    vis = d3.select("#chart").append("svg:svg")
        .attr("width", w + m[1] + m[3])
        .attr("height", h + m[0] + m[2])
      .append("svg:g")
        .attr("transform", "translate(" + m[3] + "," + m[0] + ")");

    root.x0 = h / 2;
    root.y0 = 0;
    root.children.forEach(collapse);
    update(root);

    setup_button("button#add_staff", 'ui-icon-circle-plus');
    setup_button("button#add_proc", 'ui-icon-circle-plus');
    setup_button("button#del_proc", 'ui-icon-circle-close');

    $("#choose").accordion({
        collapsible: true,
        autoHeight: false,
        create: function(event, ui) {
            $(this).accordion("activate", false);
        }
    });
    
    $("input.tile").button();

    if (!Backbone.history.start()) {
        // Default to Step 1.
        routes.navigate("step/0", true);
    }

});

