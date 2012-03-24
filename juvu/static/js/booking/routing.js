//-------------------------------------------------------
// Route URLs.
//

var routey = Backbone.Router.extend({

    routes: {
        "toc": "toc",
        "service": "service",
        "choose/:opt": "choose",
    },

    toc: function() {
        viewModel.viewing("toc");
    },

    service: function() {
        viewModel.viewing("service");
    },

    choose: function(opt) {
        viewModel.viewing("choose");
        // TODO: check opt here
        viewModel.current_filter(opt);
    },
/*
    step: function(num) {
        num = +num;
        if (num >= 0 && num <= 4) {
            viewModel.viewing(num);
        } else {
            routes.navigate("toc", true);
        }
    },
*/
});

