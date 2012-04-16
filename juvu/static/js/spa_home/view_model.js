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

    staff_classes: ko.observableArray([]),
    current_staff_class: ko.observable({name:''}),
    staff_with_class: ko.observableArray(staff),
    current_staff_member_staff_classes: ko.observableArray([]),

    // Display the time corresponding to the mouse position on the calendar pane.
    mouse_time: ko.observableArray(),

    start_time: ko.observable("now"),
    end_time: ko.observable("then"),
    block_success: false,

    clear_staff_member_form: function() {
        // Clear out the staff form.
        $("form#staff_edit").find("input[type=text]").val("");
    },

    // A bit of indirection to allow binding to this callback before current_proc is specified.
    add_subtype: function () {
        viewModel.current_proc().add_subtype();
    },

    del_subtype: function () {
        // viewModel.current_proc().add_subtype();
    },

    add_staff_member: function() {
        var name = $("#staff_f_name").val();
        if (name != "") {
            var newbie = new StaffMember({
                name: name,
                description: 'Bananas and Peanutbutter',
                extraCost: 0.25,
            })
            this.staff.push(newbie);
            this.current_staff_member(newbie);
            $("#staff_f_name").val('');
        } else {
            $("input[type=text]").effect('highlight');
        }
    },

    add_class: function() {
        var new_class = $("#id_add_class").val();
        if (!new_class) { return }
        new_class = new StaffMemberClass({name:new_class})
        viewModel.staff_classes.push(new_class);
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

