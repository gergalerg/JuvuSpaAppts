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

var StaffMemberClass = function(options) {
    this.name = options.name;
    this.remove = function() {
        viewModel.staff_classes.remove(this);
    }
}
