//-------------------------------------------------------
// Route URLs.
//

var routey = Backbone.Router.extend({

    routes: {
        'toc': 'toc',
        'service': 'service',
        'choose/:opt': 'choose',
        'inv': 'inv'
    },

    toc: function() {
        viewModel.viewing('toc');
    },

    service: function() {
        viewModel.viewing('service');
    },

    choose: function(opt) {
        viewModel.viewing('choose');
        // TODO: check opt here
        viewModel.first_choose = viewModel.first_choose || (
            ((opt == 'dis') && (viewModel.previous_filter != 'nei')) ||
            ((opt == 'nei') && (viewModel.previous_filter != 'dis')) ||
            ((opt == 'to') && (viewModel.previous_filter != 'date')) ||
            ((opt == 'date') && (viewModel.previous_filter != 'to'))
            );
        viewModel.current_filter(opt);
    },

    inv: function() {
        viewModel.viewing('inv');
    }

});

