//-------------------------------------------------------
// Tree Layout Junk.
//

/*global d3, goog, juvume,  _ */

goog.provide('juvume.TreeThing');

/**
 * @this {Object}
 * @param {*} element_selector Where to put the tree.
 * @param {*} root Top node object to render.
 * @param {*} width Width.
 * @param {*} height Height.
 */
juvume.TreeThing.init = function(element_selector, root, width, height) {

  this.root = root;
  this.tree = d3.layout.tree().size([height, width]);
  this.duration = 300;

  this.diagonal = d3.svg.diagonal().projection(function(d) {
    return [d.y, d.x];
  });

  this.treebox = d3.select(element_selector).append('svg:svg')
  .attr('width', width)
  .attr('height', height)
  .append('svg:g')
  .attr('class', 'treebox')
  .attr('transform', 'translate(100, 0)');

  root.x0 = height / 2;
  root.y0 = 0;
  _.invoke(root.children, 'collapse');

  root.collapse();
  this.update(root);
};

/**
 * @this {Object}
 */
juvume.TreeThing.first_open = _.once(function() {
  this.root.children = this.root._children;
  this.root._children = null;
  this.update(this.root);
});


/**
 * A node for the Tree Thing.
 * @constructor
 * @param {*} options Node options.
 * TODO: document node options.
 */
juvume.TreeThing.TreeNode = function(options) {
  var also_this = this;
  this.name = options.name;
  this.id = juvume.TreeThing.TreeNode.i++;

  if (!_.isUndefined(options.children)) {
    this.children = _.map(
      options.children,
      function(n) {
        var child = new juvume.TreeThing.TreeNode(n);
        child.parent = also_this;
        return child;
      }
    );
  } else {
      this.children = null;
  }

};


/**
 * @this {Object}
 * @return {Boolean} Indicates that the TreeNode is a leaf.
 */
juvume.TreeThing.TreeNode.prototype.isLeaf = function() {
  // Neither children nor _children are there.
  return _.isUndefined(this.children || this._children);
};

/**
 * Collapse node.
 * @this {Object}
 */
juvume.TreeThing.TreeNode.prototype.collapse = function() {
  if (this.children) {
    this._children = this.children;
    _.invoke(this._children, 'collapse');
    this.children = null;
  }
};

/**
 * Toggle selected state of this node.
 * @this {Object}
 */
juvume.TreeThing.TreeNode.prototype.toggleSelected = function() {
  this.selected = !this.selected;
  if (this.selected) {
    juvume.TreeThing.root.unselectOthers(this);
  }
};


/**
 * For this node and all its children recursively set selected
 * to false except for node d.
 * @param {TreeNode} d The node that was clicked.
 * @this {Object}
 */
juvume.TreeThing.TreeNode.prototype.unselectOthers = function(d) {
  this.selected = (this === d);
  if (!this.isLeaf()) {
    _.invoke((this.children || this._children), 'unselectOthers', d);
  }
};


/**
 * Due to a wrinkle in the way you bind callbacks with D3
 * this turns out to be more of a static method.
 * @param {TreeNode} d The node that was clicked.
 */
juvume.TreeThing.TreeNode.tree_node_click = function(d) {
  d.toggleSelected();
  if (!d.isLeaf()) {
    if (d.children) {
      d._children = d.children;
      d.children = null;
    } else {
      d.children = d._children;
      d._children = null;
    }
  }
  juvume.TreeThing.update(d);
};

/**
 * This integer is used to assign id attributes to TreeNode objects.
 */
juvume.TreeThing.TreeNode.i = 0;


/**
 * @return {string} the fill color (CSS) for this node.
 * @this {Object}
 */
juvume.TreeThing.TreeNode.prototype.getFill = function() {
  return this.selected ? 'lightsteelblue' : '#eef';
};


/**
 * @this {Object}
 * @param {TreeNode} source The node to use as the root if the update.
 */
juvume.TreeThing.update = function(source) {

  // Compute the new tree layout.
  var nodes = this.tree.nodes(this.root).reverse();

  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 110; });

  // Update the nodes…
  var node = this.treebox.selectAll('g.node')
    .data(nodes, function(d) { return d.id; });

  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append('svg:g')
    .attr('class', 'node')
    .attr('transform', function(d) {
      return 'translate(' +
        (source.y0 || source.y) +
        ',' +
        (source.x0 || source.x) +
        ')';
    })
    .on('click', this.TreeNode.tree_node_click);

  nodeEnter.append('svg:circle')
    .attr('r', 1e-6);

  nodeEnter.append('svg:text')
    .attr('x', function(d) { return d.isLeaf() ? 10 : -10; })
    .attr('dy', '.35em')
    .attr('text-anchor', function(d) {
      return d.isLeaf() ? 'start' : 'end';
    })
    .text(function(d) { return d.name; })
    .attr('fill', 'black')
    .attr('font-size', 16)
    .style('fill-opacity', 1e-6);

  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
    .duration(this.duration)
    .attr('transform', function(d) {
      return 'translate(' + d.y + ',' + d.x + ')';
    });

  nodeUpdate.select('circle')
    .attr('r', 8)
    .style('fill', function(d) { return d.getFill(); });

  nodeUpdate.select('text')
    .style('fill-opacity', 1);

  node.exit().map(function(d) {
    d.collapse();
    return d;
  });

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node.exit().transition()
    .duration(this.duration)
    .attr('transform', function(d) {
      return 'translate(' + source.y + ',' + source.x + ')';
    })
    .remove();

  nodeExit.select('circle')
    .attr('r', 1e-6);

  nodeExit.select('text')
    .style('fill-opacity', 1e-6);

  // Update the links…
  var link = this.treebox.selectAll('path.link')
    .data(this.tree.links(nodes), function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert('svg:path', 'g')
    .attr('class', 'link')
    .attr('d', function(d) {
      var o = {x: source.x0, y: source.y0};
      return juvume.TreeThing.diagonal({source: o, target: o});
    })
  .transition()
    .duration(this.duration)
    .attr('d', this.diagonal);

  // Transition links to their new position.
  link.transition()
    .duration(this.duration)
    .attr('d', this.diagonal);

  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
    .duration(this.duration)
    .attr('d', function(d) {
      var o = {x: source.x, y: source.y};
      return juvume.TreeThing.diagonal({source: o, target: o});
    })
    .remove();

  // Stash the old positions for transition.
  nodes.forEach(function(d) {
    d.x0 = d.x;
    d.y0 = d.y;
  });
};

