// $(".staff_cal ").each( function(i, it) {it = $(it);console.log(i, it.val(), it.attr('id'))} )
// .each( function(index, Element) )
//-------------------------------------------------------
// Miscellaneous functions.
//

function toc_in() {
    $("#toc").switchClass("seven", "two", 500, 'easeOutBounce', function() {
        $("#main_frame").fadeIn();
    });
}

function toc_out() {
    $("#main_frame").fadeOut(150, function() {
        $("#toc").switchClass("two", "seven", 150);
    });
}

function setup_button(sel, ico, show_text) {
    show_text = show_text || false;
    $(sel).button({icons: {secondary:ico}, text: show_text })
        .click(function(){return false});
}

function params_into_object(d, initial) {
    var staff_classes = [];
    _.each(d, function(foo) {
        if (foo.name.substr(0, 3) == "sc_") {
            var n = foo.name.substr(3);
            n = lookup_staff_class(n);
            staff_classes.push(n);
        } else {
            initial[foo.name] = foo.value;
        }
    });
    if (staff_classes.length > 0) {
        initial.staff_classes = staff_classes;
    }
}

function toggle_resources() {
    $("#resource_picker_inner").toggle("blind");
};

function toggle_staff_classs() {
    $("#staff_class_picker_inner").toggle("blind");
};

function toggle_addon_procs() {
    $("#addon_procs_picker_inner").toggle("blind");
};

function toggle_options_procs() {
    $("#addon_options_picker_inner").toggle("blind");
};

function clean_time(t) {
    return t;
}

function gather_schedule() {
    var sched = {}
    $(".staff_cal").each(function(i, it) {
        it = $(it);
        var k = it.attr('id');
        var v = it.val();
        console.log(i, k, v);
        sched[k] = v;
    })
    return sched;
}

function post_sched(sched) {
    $.ajax({
        url: "/spa/post_sched/",
        type: 'POST',
        data: sched,
        success: function(data, textStatus, jqXHR) {
            data = _.flatten(data);
            console.log(data);
            setup_bands(data);
            console.log("data mapped to calendar");
        },
    });
}

//post_sched(gather_schedule())

