var StaffCalendarModel = function() {

    this.mode = "null_mode";
    this.set_mode = function(mode) {
        this.mode = mode;
        $(".button_highlight_highlight").removeClass("button_highlight_highlight");
        $('#' + mode).parents(".button_highlight").addClass("button_highlight_highlight");
    }

    var me = this;
    this.select = function(start, end, allDay) { me[me.mode].select(start, end, allDay) };

    this.fullcal = setup_staff_calendar(this);

    this.gotoDate = function(d) {
        this.fullcal.fullCalendar('gotoDate', d);
    };

    this.null_mode = {
        select: function(start, end, allDay) {
            me.fullcal.fullCalendar('unselect');
        }, // select
    } // null mode

    this.block_mode = {
        select: function(start, end, allDay) {
            viewModel.start_time(start);
            viewModel.end_time(end);

            $('#yo_dialog').reveal();
            me.fullcal.fullCalendar('unselect');
            me.fullcal.fullCalendar(
            'renderEvent',
            {
                title: 'Sup homies!?',
                start: start,
                end: end,
                allDay: allDay,
                className: 'blocky'
            },
            true // make the event "stick"
            );
            me.set_mode("null_mode");
        }, // select
    } // block mode

    this.discount_mode = {
        select: function(start, end, allDay) {
            viewModel.start_time(start);
            viewModel.end_time(end);
            me.fullcal.fullCalendar('unselect');
            me.fullcal.fullCalendar(
            'renderEvent',
            {
                title: 'Aw yeah! Discount!',
                start: start,
                end: end,
                allDay: allDay,
                className: 'discounty'
            },
            true // make the event "stick"
            );
            var d = $(".discounty")
            d.find(".fc-event-inner").removeClass("fc-event-skin");
            d.find(".fc-event-head").removeClass("fc-event-skin");
            d.find(".fc-event-bg").detach();
            me.set_mode("null_mode");
            $('#yo_dialog').reveal();
        }, // select
    } // discount mode

}


function setup_cal_tools() {

    // Staff class selector.
    var f = function() { $("#fuk").text($("#ctsc").val()) };
    $("#ctsc").change(f)
    f();

    // Buttons for the different paint modes.
    $("button#block_mode").click(function(){
        console.log("Enter block mode.");
        staff_cal.set_mode("block_mode");
    })
    $("button#discount_mode").click(function(){
        console.log("Enter discount mode.");
        staff_cal.set_mode("discount_mode");
    })
}


function setup_staff_calendar(mod) {
    return $("#show").fullCalendar({
            // put your options and callbacks here
            header: {
                left: 'title',
                center: '',
                right: '',
            },
            height: 650,
            defaultView: 'agendaWeek',
            selectable: true,
            weekends: true,
            slotMinutes: 15,
            select: mod.select,
        });
}












////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Everything below here is old and should be removed (as soon as we determine that it's not being used anywhere.)

function random_apts(staff_member) {
    var res = [Math.random(), Math.random(), Math.random(), Math.random(), Math.random(), Math.random()];
    res.sort();
    res = _.map(res, day_to_n.invert);
    return [
        { start: res[0], end: res[1], staff_member: staff_member },
        { start: res[2], end: res[3], staff_member: staff_member },
        { start: res[4], end: res[5], staff_member: staff_member }
    ];
}

// var show_us = _.flatten([[], [{"start": "2011-01-01T07:00:00", "end": "2011-01-01T02:30:00", "day": "monday", "day_of_week": 0}, {"start": "2011-01-01T03:00:00", "end": "2011-01-01T18:00:00", "day": "monday", "day_of_week": 0}], [], [], [], [{"start": "2011-01-01T05:00:00", "end": "2011-01-01T12:00:00", "day": "tuesday", "day_of_week": 1}, {"start": "2011-01-01T12:01:00", "end": "2011-01-01T09:00:00", "day": "tuesday", "day_of_week": 1}], []]);

//-------------------------------------------------------
// Staff member calendar view support.
//

var color_of = d3.scale.linear()
        .domain([0, 1])
        .range(["hsl(0, 50%, 70%)", "hsl(360, 50%, 70%)"])
        .interpolate(d3.interpolateHsl);

function setup_bands(show_us) {
    var R = _.range(7);
    var x = d3.scale.ordinal()
        .domain(R)
        .rangeBands([80, 335], 0.125);
    var col = d3.scale.ordinal()
        .domain(R)
        .rangePoints([0.0, 1.0], 0.5);

    d3.select("svg")
      .selectAll("rect")
      .remove();

    d3.select("svg")
      .selectAll("rect")
      .data(show_us)
      .enter().append("svg:rect")
        .attr("x", function(d) { return x(d.day_of_week) })
        .attr("width", x.rangeBand())
        .attr("y", function(d) { return day_line(_D(d.start)) })
        .attr("height", function(d) { return day_line(_D(d.end)) - day_line(_D(d.start)) })
        .attr("fill", function(d, i) { return color_of(col(i)) })
        .on("mouseover", function(d) {
            viewModel.mouse_time(hour(_D(d.start)));
        });
}

