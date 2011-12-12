

















var DocumentView = Backbone.View.extend({

  events: {
    "dblclick"                : "open",
    "click .icon.doc"         : "select",
    "contextmenu .icon.doc"   : "showMenu",
    "click .show_notes"       : "toggleNotes",
    "click .title .lock"      : "editAccessLevel",
    "mouseover .title .date"  : "showTooltip"
  },

  render: function() {
    $(this.el).html(this.template(this.model.toJSON()));
    return this;
  },

  open: function() {
    window.open(this.model.get("viewer_url"));
  },

  select: function() {
    this.model.set({selected: true});
  },

  ...

});




















function trenche_id(trenche) {
    return $(trenche).find('h1').first().html();
}

// Various API calls that (eventually) contact the server.
var dispatch = {

    drop_attempt: function(which, where) {
        console.log('dropping', which.html(), 'in', trenche_id(where), '...');

        // if (it's already in the trenche) { return false }

        var result = false;
        $.ajax({
            type: 'POST',
            url: "{% url iapi %}",
            async: false,
            data: {
                s: which.html(),
                p: 'add_treatment_to_trenche',
                o: trenche_id(where),
            },
            success: function(data) { result = data; },
            dataType: 'json',
        });
        return result;
    },

    drop_success: function(which, where) {
	    var text = which.html();
        make_trenche_tile(where, text);
        console.log('dropped', text, 'in', trenche_id(where));
    },

    remove_attempt: function(which, where) {
        // AJAX POST to server to remove the tile from the trenche
        var s = which.find(".trenche_text").text()
        console.log("removing", s, 'from', trenche_id(where));
        return true;
    },

    remove_success: function(which, where) {
        var s = which.find(".trenche_text").text()
        console.log("removed", s, 'from', trenche_id(where));
        which.fadeOut(333, function() { which.remove() });
    },

    avail_attempt: function(trenche) {
        console.log("adding avail to", trenche);
        var data = {};
        jQuery.map($("form").serializeArray(), function(n, i){
            data[n['name']] = n['value'];
        });
        data['s'] = trenche;
        data['p'] = 'create_availability_with_trenche';
        data['o'] = null;

        var result = false;
    $.ajax({
            type: 'POST',
            url: "{% url iapi %}",
            async: false,
            data: data,
            success: function(data) { result = data; },
            dataType: 'json',
        });
        return result;
        return true;
    },

    avail_success: function(trenche) {
        console.log("added avail to", trenche);
        slide_right();
    },

};


