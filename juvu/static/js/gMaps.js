//google maps
window.onload = function()
{
	initialize();
}

function initialize() {
	var myLatlng = new google.maps.LatLng(37.78, -122.44);
	var myOptions = {
		zoom: 12,
		center: myLatlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}
	var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
	var marker = new google.maps.Marker({
		position: myLatlng,
		map: map,
		title:"Merchant Name"
	});
} 