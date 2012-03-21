viewModel = {

    // Track the current "view" the user is looking at.
    viewing: ko.observable(),

}


viewModel.viewing.subscribe(function(view) {
    console.log(view);
});

