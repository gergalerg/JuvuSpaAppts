
function create_login_circles() {
    create_login_circle(".signup_circle", circle_1_radius);
    create_login_circle(".login_circle", circle_2_radius);
    create_login_circle(".exp_circle", circle_3_radius);
}

function create_login_circle(cls, r) {
	var svg_element1 = d3.select(cls).append("svg:svg");
	svg_element1
		.attr("width", r * 2)
		.attr("height", r * 2);
	svg_element1.append("svg:circle")
		.attr("cx", r)
		.attr("cy", r)
		.attr("r", r)
		.attr("fill", "white")
		.attr("fill-opacity", 0.55);
}

var login_controls = {
    hide_signup: function() {
        $(".signup_circle").fadeOut();
        $(".s1").fadeOut();
    },

    show_signup: function() {
        $(".signup_circle").fadeIn();
        $(".s1").fadeIn();
    },

    hide_login: function() {
        $(".login_circle").fadeOut();
        $(".s2").fadeOut();
    },

    show_login: function() {
        $(".login_circle").fadeIn();
        $(".s2").fadeIn();
    },

    hide_exp: function() {
        $(".exp_circle").fadeOut();
        $(".s3").fadeOut();
    },

    show_exp: function() {
        $(".exp_circle").fadeIn();
        $(".s3").fadeIn();
    },
}


