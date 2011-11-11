$(function(){

// Swap background images
var bg_img = ["/static/bg/537183095_9b2abcba55_b.jpg", "/static/bg/3877954043_31c6cc7441_b.jpg", "/static/bg/2964708287_1a9ee41468_b.jpg"];

// Random swap function
function rdm_bg_img() {
	return bg_img[Math.floor(Math.random() * bg_img.length)];
}
 
// Assign at least one img, create this DOM on the fly next time
$("#background").attr("src", bg_img[0]);

// Key switches
$(document).keypress(function(e){
	switch(e.which)
	{
		// Background
		case 49: 
			$("#background").attr("src", bg_img[0]);
			break;	
		
		case 50: 
			$("#background").attr("src", bg_img[1]);
			break;
		
		case 51:
			$("#background").attr("src", bg_img[2]);
			break;
			
		// Logotype
		case 52:
			$("#logotype").css("font-family", "Pacifico");
			break;

		case 53:
			$("#logotype").css("font-family", "Chewy");
			break;

		case 54:
			$("#logotype").css("font-family", "Dancing Script");
			break;
	}
});

});