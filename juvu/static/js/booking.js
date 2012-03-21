
function create_login_circles() {

	var svg_element1 = d3.select(".signup_circle").append("svg:svg");
	svg_element1
		.attr("width",94)
		.attr("height",94);
	
	var circle2 = svg_element1.append("svg:circle");
	circle2
		.attr("cx", 47)
		.attr("cy", 47)
		.attr("r", 47)
		.attr("fill", "white")
		.attr("fill-opacity", 0.55);
	
	var svg_element2 = d3.select(".login_circle").append("svg:svg");
	svg_element2
		.attr("width",214)
		.attr("height",214);
	
	var circle2 = svg_element2.append("svg:circle");
	circle2
		.attr("cx", 107)
		.attr("cy", 107)
		.attr("r", 107)
		.attr("fill", "white")
		.attr("fill-opacity", 0.55);
		
	var svg_element3 = d3.select(".exp_circle").append("svg:svg");
	svg_element3
		.attr("width",110)
		.attr("height",110);
	
	var circle3 = svg_element3.append("svg:circle");
	circle3
		.attr("cx", 55)
		.attr("cy", 55)
		.attr("r", 55)
		.attr("fill", "white")
		.attr("fill-opacity", 0.55);
}

