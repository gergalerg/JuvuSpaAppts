

var results = [
    {
        name: "Barney",
        price: 23.00,
        discount: "",
    },
]

var ResultThing = function(options) {

    this.name = options.name;
    this.price = options.price;
    this.discount = options.discount;

    this.book = function() {
    }

    this.bid = function() {
    }
}

var MODEL = {
    results: ko.observableArray(),
}

MODEL.set_results = function(res) {
    MODEL.results(res)
}

MODEL.wire_up_buttons = function(elements) {
    var buttons = $(elements).find(".b_btn")
    var us = buttons.parent().find(".service, .price, .discount");
    buttons.mouseover(function(){
		us.css({'background-color':'#C6E6FC'})
	});
	buttons.mouseout(function(){
		us.css({'background-color':'white'})
	});
}

MODEL.set_results(_.map(results, function(data){ return new ResultThing(data) }));

