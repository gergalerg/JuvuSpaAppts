function form_into_object(form, obj) {
    _.each(form.serializeArray(), function(foo) { obj[foo.name] = foo.value });
}

function collect_options() {
    var params = {};
    form_into_object($("form.dis_form"), params);
    form_into_object($("form.nei_form"), params);
    form_into_object($("form.date_form"), params);
    form_into_object($("form.opts_form"), params);
    return params;
}

function clicky(selector, route) {
    $(selector).click(function() { routes.navigate(route, true); })
}

function setup_option_circles(ops_canvas) {
    console.log("setup_option_circles");

    $("#id_miles").keyup(function () {
        if ($(this).val().length > 0) {
            reveal_when_circles()
        }
    });
    $("form.nei_form").find("input[type=checkbox]").click(reveal_when_circles);
    $("form.date_form").find("input[type=textarea]").click(reveal_option_circle);
    clicky(".distance > span.pointy", "choose/dis");
    clicky(".neighbor > span.pointy", "choose/nei");
    clicky(".date > span.pointy", "choose/date");
    clicky(".option > span.pointy", "choose/opts");


	var svg_canvas = d3.select(ops_canvas).append("svg:svg");
	svg_canvas
	  .attr("width", 1024)
	  .attr("height", 768)
	  .attr("class", "s_canvas");
	
	//Neighborhood
	svg_canvas.append("svg:circle")
	  .attr("cx",535)
	  .attr("cy",233)
	  .attr("r",65)
	  .attr("fill",second_color)
	  .attr("fill-opacity",1)
	  .attr("class","c_nei pointy")
	  .on("click", function(){
	      routes.navigate("choose/nei", true);
	  });
	
	//distance
	svg_canvas.append("svg:circle")
	  .attr("cx",450)
	  .attr("cy",170)
	  .attr("r",65)
	  .attr("fill",first_color)
	  .attr("fill-opacity",1)
	  .attr("class","c_dis pointy")
	  .on("click", function(){
	      routes.navigate("choose/dis", true);
	  });
	
	//today
	svg_canvas.append("svg:circle")
	  .attr("cx",870)
	  .attr("cy",300)
	  .attr("r",0)
	  .attr("fill",first_color)
	  .attr("fill-opacity",0)
	  .attr("class","c_to pointy")
	  .on("click", function(){
	    // FIXME: Do something intelligent here.
	  });
	
	//Date range
	svg_canvas.append("svg:circle")
	  .attr("cx",955)
	  .attr("cy",363)
	  .attr("r",0)
	  .attr("fill",second_color)
	  .attr("fill-opacity",0)
	  .attr("class","c_date pointy")
	  .on("click", function(){
	    routes.navigate("choose/date", true);
	  });
	
	//option
	svg_canvas.append("svg:circle")
		.attr("cx",800)
		.attr("cy",350)
		.attr("r",0)
		.attr("fill",first_color)
		.attr("fill-opacity",0)
		.attr("class","c_op pointy")
		.on("click", function(){
	      routes.navigate("choose/opts", true);
		});
	
	//juvu me
	svg_canvas.append("svg:circle")
		.attr("cx",950)
		.attr("cy",350)
		.attr("r",0)
		.attr("fill",second_color)
		.attr("fill-opacity",0)
		.attr("class","c_me pointy")
		.on("click", function(){
		    routes.navigate("inv", true);
		})
		
}
