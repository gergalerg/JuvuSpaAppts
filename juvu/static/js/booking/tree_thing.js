//-------------------------------------------------------
// Tree Layout Junk.
//

var tree = d3.layout.tree()
    .size([700, w]);

var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.y, d.x]; });

function setup_tree_thing(element_selector, root) {
    vis2 = d3.select(element_selector).append("svg:svg")
        .attr("width", w + m[1] + m[3])
        .attr("height", 800)
      .append("svg:g")
        .attr("class", "treebox")
        .attr("transform", "translate(" + m[3] + "," + m[0] + ")");
    root.x0 = h / 2;
    root.y0 = 0;
    root.children.forEach(collapse);
    collapse(root);
    update(root);
    //change default selection
    $("#tree").append('<div id="goey"><a href="/look/#choose/nei" class="blue_button">Cool! Let&rsquo;s find that for you</a></div>');
    $("#goey").hide();
    $("#tree").hide();
}

var open_treething = _.once(function(){
    root.children = root._children;
    root._children = null;
    update(root);
});

// Toggle tree children on click.
function tree_node_click(d) {
  if (d.is_leaf()) {
    d.supported(!d.supported());
    if (d.supported()) {
        d.make_current();
    } else {
        viewModel.current_proc({name:''});
    };
    if (_.has(d, "parent")) { unselect_other(d.parent, d); };

  } else if (d.children) {
    d.supported(!d.supported());
    if (_.has(d, "parent")) { unselect_other(d.parent, d); };
    d._children = d.children;
    d.children = null;

  } else {
    d.children = d._children;
    d._children = null;
  }

  set_amenities(d)
  update(d);
}

function attach_parents(n) {
    if (!_.has(n, "children")) { return };
    _.map(n.children, function(child) { child.parent = n; });
}

function unselect_other(me, d) {
    var ginger = _.filter(me.children, function(child) { return (d !== child) })
    _.map(ginger, unselecty);
    if (_.has(me, "parent")) { unselect_other(me.parent, me); };
}

function unselecty(d) {
    d.supported(false);
    if (_.has(d, "children")) { _.map(d.children, unselecty); };
}

function set_amenities(d) {
  console.log("set_amenities", d);
  if (_.has(d, "amenities")) {
    update_amenities(d.amenities)
  } else {
    if (_.has(d, "parent")) { set_amenities(d.parent); };
  }
}

function collapse(d) {
    if (d.children) {
      d._children = d.children;
      _.each(d._children, collapse);
      d.children = null;
    }
}

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
          if (_.has(d, "supported") && d.supported()) {
              return "lightsteelblue";
          }
          return "#eef";
      });

  nodeUpdate.select("text")
      .style("fill-opacity", 1);

  node.exit().map(function(d) {
    collapse(d);
    if (_.has(d, "supported")) { d.supported(false) }
    return d;
  });

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

