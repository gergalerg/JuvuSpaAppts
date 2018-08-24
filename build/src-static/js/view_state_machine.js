//-------------------------------------------------------
// A generic state machine with transitions in and out.
//

/*global goog, juvume,  _ */

goog.provide('juvume.ViewStateMachine');

/**
 * A State Machine class for handling view transitions.
 * @constructor
 * @param {Object} view_transitions An object mapping view names to functions.
 * @param {Object} hide_transitions An object mapping view names to functions.
 * @param {String} initital_view The view that we're looking at now.
 */
juvume.ViewStateMachine = function(
	view_transitions,
	hide_transitions,
	initital_view) {
  this.previous_view = initital_view;
  this.view_transitions = view_transitions;
  this.hide_transitions = hide_transitions;
};

/**
 * Trigger the hide transition for the previous view. This is
 * an internal method and should be considered "private".
 * @this {ViewStateMachine}
 */
juvume.ViewStateMachine.prototype.do_hide = function() {
  var old_view = this.previous_view;
  if (!!old_view || _.has(this.hide_transitions, old_view)) {
    this.hide_transitions[old_view]();
  }
};

/**
 * Trigger the hide transition for the previous view.
 * @this {ViewStateMachine}
 * @param {String} view Switch to this view.
 * @return {Boolean} Indicates if transition actually occurs.
 */
juvume.ViewStateMachine.prototype.do_view = function(view) {
  if (view === this.previous_view || !_.has(this.view_transitions, view)) {
    return false;
  }
  this.do_hide();
  this.view_transitions[view]();
  this.previous_view = view;
  return true;
};

