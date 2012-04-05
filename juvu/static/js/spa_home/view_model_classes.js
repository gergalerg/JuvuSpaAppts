//-------------------------------------------------------
// View Model Classes
//

function set_em(thing, from, field, orthis) {
    var value = _.isUndefined(from[field]) ? orthis : from[field];
    if (_.isArray(value)) {
        thing[field] = ko.observableArray(value);
    } else {
        thing[field] = ko.observable(value);
    }
}


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

    set_em(this, options, 'nickname', "");
    set_em(this, options, 'price', 0.0);
    set_em(this, options, 'duration', 60);
    set_em(this, options, 'subtypes', []);
    set_em(this, options, 'staff_classes', []);

    var also_this = this; // TODO: look up how to do this properly,
    _.each(this.staff_classes(), function(staff_class) {
        staff_class.procs.push(also_this);
    })

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

var StaffMemberClass = function(options) {
    this.name = options.name;
    set_em(this, options, 'procs', []);
    this.remove = function() {
        viewModel.staff_classes.remove(this);
    }
}

function lookup_staff_class(class_name) {
    SC = _.find(viewModel.staff_classes(), function (staff_class) {
        return class_name == staff_class.name;
    });
    // TODO: handle non-found class_name.
    console.log(SC);
    return SC;
}

