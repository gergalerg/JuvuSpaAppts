function DisplayCircle(){};


var choose_view_transitions = {
    dis: function() {
        options_transitions.clickDis();
        if (viewModel.first_choose) {
            options_transitions.little_show_nei()
            viewModel.first_choose = false;
        }
    },
    nei: function() {
        options_transitions.clickNei();
        if (viewModel.first_choose) {
            options_transitions.little_show_dis()
            viewModel.first_choose = false;
        }
    },
}

var choose_unview_transitions = {
    dis: function() {
        if (viewModel.current_filter() == "nei") {
            options_transitions.little_show_dis()
        } else {
            options_transitions.hide_dis();
        }
    },
    nei: function() {
        if (viewModel.current_filter() == "dis") {
            options_transitions.little_show_nei()
        } else {
            options_transitions.hide_nei();
        }
    },
}


function choose_unview() {
    var old_filter = viewModel.previous_filter;
    viewModel.previous_filter = viewModel.current_filter();
    if (old_filter == "") {
        return;
    }
    if (!_.has(choose_unview_transitions, old_filter)) {
        console.log("unknown choose_unview", old_filter);
        return;
    }
    console.log("choose_unviewing", old_filter);
    var f = choose_unview_transitions[old_filter];
    f();
}

viewModel.current_filter.subscribe(function(filter) {
    console.log("choose_viewing", filter);
    choose_unview();
    if (!_.has(choose_view_transitions, filter)) {
        console.log("unknown filter", filter);
        routes.navigate("toc", true);
        return;
    }
    var f = choose_view_transitions[filter];
    f();
});


var options_transitions = {

    clickDis: function() {
        $(".c_dis").appendTo($(".s_canvas"));
	  	d3.select(".c_dis").transition()
	  		.attr("cx", 450)
	  		.attr("cy", 230)
	  		.attr("r", 200)
	  		.attr("fill", first_color)
	  		.duration(1000)
	  		.ease("elastic", 5, 3);

	  	d3.select(".distance").transition()
	  		.style("left","305px")
	  		.style("top","170px")
	  		.duration(1000)
	  		.ease("elastic", 5, 3)
          .transition()
	  		.style("display","block")
	  		.style("opacity", 1)
	  		.delay(1000)
	  		.duration(300);

	  	d3.select(".dis_form").transition()
	  		.style("display","block")
	  		.style("opacity","1")
	  		.duration(500)
	  		.delay(500);
	},

	hide_dis: function() {

	},

	little_show_dis: function() {
	  	d3.select(".c_dis").transition()
	  		.attr("cx", 305)
	  		.attr("cy", 110)
	  		.attr("r", 65)
	  		.duration(1000)
	  		.ease("elastic", 5, 4);
	  	
	  	d3.select(".distance").transition()
	  		.style("display","block")
	  		.style("left","155px")
	  		.style("top","105px")
	  		.duration(1000)
	  		.ease("elastic", 5, 4)
	  	  .transition()
	  		.style("display","block")
	  		.style("opacity","1")
	  		.delay(1000)
	  		.duration(300);

	  	d3.select(".dis_form").transition()
	  		.style("display","none")
	  		.style("opacity","0")
	  		.duration(500);
	},

	little_show_nei: function() {
	  	d3.select(".c_nei").transition()
	  		.attr("cx", 615)
	  		.attr("cy", 410)
	  		.attr("r", 65)
	  		.duration(1000)
	  		.ease("elastic", 5, 4);

	  	d3.select(".neighbor").transition()
	  		.style("left"," 442px")
	  		.style("top"," 400px")
	  		.style("display","none")
	  		.style("opacity",0)
	  		.duration(1000)
	  		.ease("elastic", 5, 4)
          .transition()
	  		.style("display","block")
	  		.style("opacity","1")
	  		.delay(1000)
	  		.duration(300);

	  	d3.select(".nei_form").transition()
	  		.style("display","none")
	  		.style("opacity","0")
	  		.duration(500);
	},

	clickNei: function() {

        $(".c_nei").appendTo($(".s_canvas"));
	  	d3.select(".c_nei").transition()
	  		.attr("cx", 500)
	  		.attr("cy", 300)
	  		.attr("r", 235)
	  		.attr("fill",second_color)
	  		.duration(1000)
	  		.ease("elastic", 5, 4);
	  	
	  	d3.select(".neighbor").transition()
	  		.style("left"," 327px")
	  		.style("top"," 170px")
	  		.duration(1000)
	  		.ease("elastic", 5, 4);
	  	
	  	d3.select(".nei_form").transition()
	  		.style("display","block")
	  		.style("opacity","1")
	  		.duration(500)
	  		.delay(500);

	  	d3.select(".neighbor").transition()
	  		.style("display","block")
	  		.style("opacity", 1)
	  		.delay(1000)
	  		.duration(300);
	},

	hide_nei: function() {

	},
}
