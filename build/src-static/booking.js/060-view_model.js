viewModel = {

    // Track the current "view" the user is looking at.
    viewing: ko.observable(),
    previous_view: 'toc', // What the user was looking at last.

    // Track the current filter with which the user is working.
    current_filter: ko.observable(),
    // dis, nei, today, date, op
    previous_filter: '', // What the user was looking at last.
    first_choose: false, // Needed to flag first "entrance" to '/#choose' space.

    // Which procedure has the user selected?
    current_proc: ko.observable({name: ''})

};

function look() {
    var sf = $("form#submitter");
    sf.find("#id_proc").val(viewModel.current_proc().name);
    sf.find("#from_date_sub").val($("#from_date_cal").val());
    sf.find("#to_date_sub").val($("#to_date_cal").val());
    sf.submit();
//    window.location.href = "/look/inv";
}

var view_transitions = {
    toc: function() {
        login_controls.show();
        $('#backstretch').animate({opacity: 1.0});
    },
    service: function() {
        $('#tree').fadeIn(open_treething);
    },
    choose: function() {
        $('.wrapper').fadeIn();
    },
};

var unview_transitions = {
    toc: function() {
        login_controls.hide();
        $('#backstretch').animate({opacity: 0.3});
    },
    service: function() {
        $('#tree').fadeOut();
    },
    choose: function() {
        $('.wrapper').fadeOut();
    },
};

function unview() {
    var old_view = viewModel.previous_view;
    viewModel.previous_view = viewModel.viewing();
    if (old_view == '') {
        return;
    }
    if (!_.has(unview_transitions, old_view)) {
        console.log('unknown unview', old_view);
        return;
    }
    console.log('unviewing', old_view);
    var f = unview_transitions[old_view];
    f();
}

viewModel.viewing.subscribe(function(view) {
    console.log('viewing', view);
    viewModel.first_choose = true;
    unview();
    if (!_.has(view_transitions, view)) {
        console.log('unknown view', view);
        routes.navigate('toc', true);
        return;
    }
    var f = view_transitions[view];
    f();
});


// Show or hide the "Go" button depending on whether a procedure has
// been selected.
viewModel.current_proc.subscribe(function(proc) {
    if (!!proc.name) {
        $('#goey').fadeIn();
    } else {
        $('#goey').fadeOut();
    }
});

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
        this.nickname = ko.observable('');
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
        return '$' + (+this.price()).toFixed(0);
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
        var new_subtype = $('form#add_subtype').serializeArray();
        var n = {name: this.name, supported: true, subtypes: this.subtypes};
        params_into_object(new_subtype, n);
        console.log(n);
        var newb = new SpaProcedure(n);
        this.subtypes.push(newb);
        viewModel.supported_procs.push(newb);
        this.nickname('');
    }

    this.is_leaf = function() {
        // Neither children nor _children are there.
        return ((
            _.isNull(this.children) || _.isUndefined(this.children)
        ) && (
            _.isNull(this._children) || _.isUndefined(this._children)
        ));
    }
};

