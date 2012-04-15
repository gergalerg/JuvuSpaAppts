

var FAKE_TREATMENT_RESULTS = [
    {   name: "Barney",
        price: 23.00,
        discount: "",
        },
    ];

var results = [
    {
        name: "Barney HAZ SPA!",
        results: FAKE_TREATMENT_RESULTS
    },
];

var MerchantThing = function(options) {
    this.name = options.name;
    this.logo_image_URL = "/static/image/login_05.jpg";
    var res = _.map(
        options.results,
        function(data) { return new ResultThing(data) }
        );
    this.results = ko.observableArray(res);
    this.wire_up_buttons = function(elements) {
        var buttons = $(elements).find(".b_btn")
        var us = buttons.parent().find(".service, .price, .discount");
        buttons.mouseover(function() { us.css({'background-color':'#C6E6FC'}); });
	    buttons.mouseout(function() { us.css({'background-color':'white'}); });
    }
}

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

MODEL.set_results(_.map(results, function(data){ return new MerchantThing(data) }));


function changeColor(o) {
	oc = o.attr('fill');
	o.attr('fill', hover_color);
	return oc;
}

function changeBack(t) {
	t.attr('fill',oc);
}

function clickNeighbor() {
	$('.c_nei').appendTo($('.s_canvas'));
	//circle and text "where" disappear
	$('.where').css({'display':'none'});
	d3.select('.c_where').transition()
		.attr('r', 0)
		.duration(250);
  	
  	//show distance & neighborhood circles + texts
  	d3.select('.c_dis').transition()
  		.attr("cy",80)
  		.attr('r', 65)
		.duration(500)
  		.ease("elastic", 5, 4);
  		
  	d3.select('.c_nei').transition()
  		.attr("cy",130)
  		.attr('r', 65)
		.duration(500)
  		.ease("elastic", 5, 4);
  		
  	d3.select('.distance').transition()
  		.style('top','75px')
  		.style('display','block')
  		.style('opacity', 1)
  		.duration(500)
  		.ease("elastic", 5, 4);
  	
  	d3.select('.neighbor').transition()
  		.style('top','125px')
  		.style('display','block')
  		.style('opacity', 1)
  		.duration(500)
  		.ease("elastic", 5, 4);
  	
  	//form
  	$('.dis_form').css({'display':'none','opacity':'0'});
  	d3.select('.nei_form').transition()
  		.style('display','block')
  		.style('opacity', 1)
  		.duration(500)
  		.delay(250);
  	
  	//hide
  	hide_optionList();
	hide_todayDate();
	
  	//move "when" & "options" circles + texts 		  	
  	d3.select('.c_when').transition()
  		.attr('cy', 620)
  		.attr("r",c_size)
  		.duration(1000)
  		.ease("elastic", 5, 4);
  		
  	d3.select('.c_op').transition()
  		.attr('cy', 720)
  		.attr("r",c_size)
  		.duration(1000)
  		.ease("elastic", 5, 4);
  	
  	d3.select('.when').transition()
  		.style('display', 'block')
  		.style('top', '613px')
  		.duration(1000)
  		.ease("elastic", 5, 4);
  	
  	d3.select('.option').transition()
  		.style('top', '713px')
  		.duration(1000)
  		.ease("elastic", 5, 4);
}

function clickDistance() {
	$('.c_dis').appendTo($('.s_canvas'));
	//circle and text "where" disappear
	$('.where').css({'display':'none'});
	d3.select('.c_where').transition()
		.attr('r', 0)
		.duration(250);
	
	//show distance & neighborhood circles + texts
  	d3.select('.c_dis').transition()
  		.attr('cy', 130)
  		.attr('r', 65)
		.duration(500)
  		.ease("elastic", 5, 4);
  		
  	d3.select('.c_nei').transition()
  		.attr('cy', 70)
  		.attr('r', 65)
		.duration(500)
  		.ease("elastic", 5, 4);
  		
  	d3.select('.distance').transition()
  		.style('top','125px')
  		.style('display','block')
  		.style('opacity', 1)
  		.duration(500)
  		.ease("elastic", 5, 4);
  	
  	d3.select('.neighbor').transition()
  		.style('top','65px')
  		.style('display','block')
  		.style('opacity', 1)
  		.duration(500)
  		.ease("elastic", 5, 4);
	
	//form
	$('.nei_form').css({'display':'none','opacity':'0'});
  	d3.select('.dis_form').transition()
  		.style('display','block')
  		.style('opacity', 1)
  		.duration(500)
  		.delay(250);
	
	//hide
  	hide_optionList()
	hide_todayDate();
	
	
	//move "when" & "options" circles + texts 		  	
  	d3.select('.c_when').transition()
  		.attr('cy', 350)
  		.attr("r",c_size)
  		.duration(1000)
  		.ease("elastic", 5, 4);
  		
  	d3.select('.c_op').transition()
  		.attr('cy', 450)
  		.attr("r",c_size)
  		.duration(1000)
  		.ease("elastic", 5, 4);
  	
  	d3.select('.when').transition()
  		.style('display', 'block')
  		.style('top', '343px')
  		.duration(1000)
  		.ease("elastic", 5, 4);
  	
  	d3.select('.option').transition()
  		.style('top', '443px')
  		.duration(1000)
  		.ease("elastic", 5, 4);
}


function clickDate() {
	$('.c_date').appendTo($('.s_canvas'));
	
	$('.when').css({'display':'none'});
	d3.select('.c_when').transition()
		.attr('r', 0)
		.duration(250);
	
	//circles & texts of today & date range
	d3.select('.c_today').transition()
  		.attr('cy', 240)
  		.attr('r', 65)
		.duration(500)
  		.ease("elastic", 5, 4);
  		
  	d3.select('.c_date').transition()
  		.attr('cy', 300)
  		.attr('r', 65)
		.duration(500)
  		.ease("elastic", 5, 4);
	
	d3.select('.today').transition()
  		//.style('top','125px')
  		.style('display','block')
  		.style('opacity', 1)
  		.duration(500)
  		.ease("elastic", 5, 4);
  	
  	d3.select('.date').transition()
  		//.style('top','65px')
  		.style('display','block')
  		.style('opacity', 1)
  		.duration(500)
  		.ease("elastic", 5, 4);
	
	//form
  	d3.select('.date_form').transition()
  		.style('display','block')
  		.style('opacity', 1)
  		.duration(500)
  		.delay(250);
	
	//hide
	hide_disNei();
	hide_optionList()
	
	//show circle and text of 'where'
	original_where();
	
	//move down "options" circles + texts 		  	 		  		
  	d3.select('.c_op').transition()
  		.attr('r', c_size)
  		.attr('cy', 510)
  		.duration(1000)
  		.ease("elastic", 5, 4);
  	d3.select('.option').transition()
  		.style('top', '503px')
  		.duration(1000)
  		.ease("elastic", 5, 4);
}

function clickOption() {
	//hide forms and circles
  	hide_todayDate();
  	hide_disNei();
  	
  	//show when & where circles
  	original_where();
  	original_when();
  	
	d3.select('.c_op').transition()
		.attr("cx",150)
		.attr("cy",330)
		.attr("r",65)
		.duration(500)
  		.ease("elastic", 5, 4);
  	d3.select('.option').transition()
		.style('top','323px')
		.duration(500)
  		.ease("elastic", 5, 4);
  	d3.select('.op_list').transition()
  		.style('display','block')
  		.style('opacity','1')
  		.delay(250)
  		.duration(500);
}

//show original three circles & texts
function original() {	
	//hide
	hide_disNei();
	hide_todayDate();
	hide_optionList()
	
	//show when, where and options circles
	original_where();
  	original_when();
  	
  	d3.select('.c_op').transition()
  		.attr('r', c_size)
  		.attr('cy', 300)
  		.duration(500)
  		.ease('elastic', 5, 4);
	d3.select('.option').transition()
  		.style('display', 'block')
  		.style('opacity', 1)
  		.style('top','293px')
  		.duration(500)
  		.ease('elastic', 5, 4);
}

function hide_disNei() {
	$('.distance, .neighbor, .nei_form, .dis_form').css({'display':'none','opacity':'0'});
	d3.select('.c_dis').transition()
  		.attr('r',0)
  		.duration(500);
  	d3.select('.c_nei').transition()
  		.attr('r',0)
  		.duration(500);
}

function hide_todayDate() {
	$('.date, .today, .date_form').css({'display':'none','opacity':'0'});
	d3.select('.c_today').transition()
		.attr('r', 0)
		.duration(500);
	d3.select('.c_date').transition()
		.attr('r', 0)
		.duration(500);
}

function hide_optionList() {
	$('.op_list').css({'display':'none','opacity':'0'});
}

function original_where()
{
	d3.select('.c_where').transition()
  		.attr('r', c_size)
  		.duration(500)
  		.ease('elastic', 5, 4);	
  	d3.select('.where').transition()
  		.style('display', 'block')
  		.style('opacity', 1)
  		.duration(500)
  		.ease('elastic', 5, 4);
}

function original_when() {
	d3.select('.c_when').transition()
  		.attr('r', c_size)
  		.attr('cy', 200)
  		.duration(500)
  		.ease('elastic', 5, 4);
  	
  	d3.select('.when').transition()
  		.style('display', 'block')
  		.style('opacity', 1)
  		.style('top','193px')
  		.duration(500)
  		.ease('elastic', 5, 4);
}

