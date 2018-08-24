//-------------------------------------------------------
// Animate color cycle.
//

/*global d3, goog */

goog.provide('crambery');

goog.require('goog.Timer');

/**
 * Color interpolator.
 */
crambery.cram_color = d3.scale.linear().domain([0, 11]).range(
        ['hsl(0, 50%, 90%)', 'hsl(360, 50%, 90%)']
    ).interpolate(d3.interpolateHsl);

/**
 * Start the color cycling effect.
 * @param {number} minutes How many minutes for the whole cycle.
 * @this {Object}
 */
crambery.start = function(minutes) {
    this.timer = new goog.Timer(60000 * minutes);
    this.twelfth = 5000 * minutes;
    goog.events.listen(this.timer, goog.Timer.TICK, this.trigger);
    this.timer.start();
}

/**
 * Set up one color wheel cycle.
 * @this {Object}
 */
crambery.trigger = function() {
    'use strict';
    var i, body = d3.select('body');
    for (i = 0; i < 12; i++) {
        body.transition()
            .delay(this.twelfth * i)
            .duration(this.twelfth)
            .style('background-color', this.cram_color(i));
    }
};

goog.exportSymbol('crambery', crambery);

