//-------------------------------------------------------
// Route URLs.
//

var routey = Backbone.Router.extend({

    routes: {
        "toc": "toc",
        "step/:num": "step",
    },

    toc: function() {
        viewModel.viewing("0");
    },

    step: function(num) {
        num = +num;
        if (num >= 0 && num <= 4) {
            viewModel.viewing(num);
        } else {
            routes.navigate("toc", true);
        }
    },

});

