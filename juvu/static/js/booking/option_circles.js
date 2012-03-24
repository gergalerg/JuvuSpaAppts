function setup_option_circles(ops_canvas) {
    console.log("setup_option_circles");

	var svg_canvas = d3.select(ops_canvas).append("svg:svg");
	svg_canvas
	  .attr("width", 1024)
	  .attr("height", 768)
	  .attr("class", "s_canvas");
	
	//distance
	svg_canvas.append("svg:circle")
	  .attr("cx",450)
	  .attr("cy",170)
	  .attr("r",65)
	  .attr("fill",first_color)
	  .attr("fill-opacity",1)
	  .attr("class","c_dis")
	  .on("click", function(){
	      routes.navigate("choose/dis", true);
	    /*
	  	clickDis();
	  	disClicked = true;
	  	neiClicked = false;
	  	if(dateClicked == true)
	  	{
	  		runDate();
	  	};
	  	if(opClicked == true)
	  	{
	  		runOption();
	  	};
	  	*/
	  });
	
	//Neighborhood
	svg_canvas.append("svg:circle")
	  .attr("cx",535)
	  .attr("cy",233)
	  .attr("r",65)
	  .attr("fill",second_color)
	  .attr("fill-opacity",1)
	  .attr("class","c_nei")
	  .on("click", function(){
	      routes.navigate("choose/nei", true);
	    /*
	  	clickNei();
	  	neiClicked = true;
	  	disClicked = false;
	  	if(dateClicked == true)
	  	{
	  		runDate();
	  	};
	  	if(opClicked == true)
	  	{
	  		runOption();
	  	};
	  	*/
	  });

	//today
	svg_canvas.append("svg:circle")
	  .attr("cx",820)
	  .attr("cy",550)
	  .attr("r",0)
	  .attr("fill",first_color)
	  .attr("fill-opacity",0)
	  .attr("class","c_to")
	  .on("click", function(){
	    viewModel.current_filter("today");
	    /*
		if(disClicked == true){
			runDis();
		}else if(neiClicked == true){
			runNei();
		}
		clickToday();
		dateClicked = true;
		
		if(opClicked == true)
	  	{
	  		runOption();
	  	}else{
	  		showOption();
	  	}
	  	*/
	  });
	
	//Date range
	svg_canvas.append("svg:circle")
	  .attr("cx",905)
	  .attr("cy",613)
	  .attr("r",0)
	  .attr("fill",second_color)
	  .attr("fill-opacity",0)
	  .attr("class","c_date")
	  .on("click", function(){
	    viewModel.current_filter("dis");
	    /*
	  	if(disClicked == true){
			runDis();
		}else if(neiClicked == true){
			runNei();
		}
		clickDate();
		dateClicked = true;
		
		if(opClicked == true)
	  	{
	  		runOption();
	  	}else{
	  		showOption();
	  	}
	  	*/
	  });
	
	//option
	svg_canvas.append("svg:circle")
		.attr("cx",800)
		.attr("cy",650)
		.attr("r",0)
		.attr("fill",first_color)
		.attr("fill-opacity",0)
		.attr("class","c_op")
		.on("click", function(){
	    viewModel.current_filter("dis");
	    /*
			if(disClicked == true){
				runDis();
			}else if(neiClicked == true){
				runNei();
			}
			
			if(dateClicked == true)
			{
				runDate();
			};
			opClicked = true;
			clickOption();
	  	*/
		});
	
	//juvu me
	svg_canvas.append("svg:circle")
		.attr("cx",950)
		.attr("cy",650)
		.attr("r",0)
		.attr("fill",second_color)
		.attr("fill-opacity",0)
		.attr("class","c_me")
		.on("click", function(){
			
		})
		
}
