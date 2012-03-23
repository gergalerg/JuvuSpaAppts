
function create_login_circles() {


	var svg_element1 = d3.select(".signup_circle").append("svg:svg");
	svg_element1
		.attr("width", circle_1_radius * 2)
		.attr("height", circle_1_radius * 2);
	
	var circle2 = svg_element1.append("svg:circle");
	circle2
		.attr("cx", circle_1_radius)
		.attr("cy", circle_1_radius)
		.attr("r", circle_1_radius)
		.attr("fill", "white")
		.attr("fill-opacity", 0.55);
	

	var svg_element2 = d3.select(".login_circle").append("svg:svg");
	svg_element2
		.attr("width", circle_2_radius * 2)
		.attr("height", circle_2_radius * 2);
	
	var circle2 = svg_element2.append("svg:circle");
	circle2
		.attr("cx", circle_2_radius)
		.attr("cy", circle_2_radius)
		.attr("r", circle_2_radius)
		.attr("fill", "white")
		.attr("fill-opacity", 0.55);
		

	var svg_element3 = d3.select(".exp_circle").append("svg:svg");
	svg_element3
		.attr("width", circle_3_radius * 2)
		.attr("height", circle_3_radius * 2);
	
	var circle3 = svg_element3.append("svg:circle");
	circle3
		.attr("cx", circle_3_radius)
		.attr("cy", circle_3_radius)
		.attr("r", circle_3_radius)
		.attr("fill", "white")
		.attr("fill-opacity", 0.55);
}

