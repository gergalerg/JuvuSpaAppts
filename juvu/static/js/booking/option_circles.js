function setup_option_circles() {
	var svg_canvas = d3.select(".canvas").append("svg:svg");
	svg_canvas
	  .attr("width", 1024)
	  .attr("height", 768)
	  .attr("class", "s_canvas");
	
	//distance
	var circle = svg_canvas.append("svg:circle");
	circle
	  .attr("cx",450)
	  .attr("cy",170)
	  .attr("r",65)
	  .attr("fill",first_color)
	  .attr("fill-opacity",1)
	  .attr("class","c_dis")
	  .on("click", function(){
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
	  });
	
	//Neighborhood
	var circle = svg_canvas.append("svg:circle");
	circle
	  .attr("cx",535)
	  .attr("cy",233)
	  .attr("r",65)
	  .attr("fill",second_color)
	  .attr("fill-opacity",1)
	  .attr("class","c_nei")
	  .on("click", function(){
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
	  });

	//today
	var circle = svg_canvas.append("svg:circle");
	circle
	  .attr("cx",820)
	  .attr("cy",550)
	  .attr("r",0)
	  .attr("fill",first_color)
	  .attr("fill-opacity",0)
	  .attr("class","c_to")
	  .on("click", function(){
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
	  });
	
	//Date range
	var circle = svg_canvas.append("svg:circle");
	circle
	  .attr("cx",905)
	  .attr("cy",613)
	  .attr("r",0)
	  .attr("fill",second_color)
	  .attr("fill-opacity",0)
	  .attr("class","c_date")
	  .on("click", function(){
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
	  });
	
	//option
	var circle = svg_canvas.append("svg:circle");
	circle
		.attr("cx",800)
		.attr("cy",650)
		.attr("r",0)
		.attr("fill",first_color)
		.attr("fill-opacity",0)
		.attr("class","c_op")
		.on("click", function(){
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
		});
	
	//juvu me
	var circle = svg_canvas.append("svg:circle");
	circle
		.attr("cx",950)
		.attr("cy",650)
		.attr("r",0)
		.attr("fill",second_color)
		.attr("fill-opacity",0)
		.attr("class","c_me")
		.on("click", function(){
			
		})
		
}
