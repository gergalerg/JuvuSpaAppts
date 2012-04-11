//-------------------------------------------------------
// Date Formatting and Scales.
//

var day = d3.time.format("%w"),
    week = d3.time.format("%U"),
    _month = d3.time.format("%m"),
    mday = d3.time.format("%d"),
    yday = d3.time.format("%j"),
    format = d3.time.format("%A\n%B %d %Y"),
    wday_format = d3.time.format("%A"),
    day_format = d3.time.format("%B %d %Y");

function month(d) { return _month(d) - 1 }

//-------------------------------------------------------
// Teh Year Data.
//

var year = d3.time.days(new Date(2012, 0, 1), new Date(2013, 0, 1));
var ydata = jQuery.map(year, function(d, i) {
    var datum = {
        "month": month(d),
        "week_of_year": +week(d),
        "day_of_week": day(d),
        "day_of_month": mday(d),
        "day_of_year": +yday(d),
        "label": format(d),
        "weekday_label": wday_format(d),
        "day_label": day_format(d),
        "date": d,
    };
    var months_week = week(new Date(2012, datum.month, 1));
    datum.week_of_month = datum.week_of_year - months_week;
    return datum;
});

//-------------------------------------------------------
// Mouse bindings for the day-circles.
// Mostly to de-couple the viewModel logic from the d3 transitions that
// animate it.

function mouse_bindings(T) { T
	.on("mouseover", function(d) {
        viewModel.pointed_at(d.label);
        viewModel.pointed_at_el(this);
    })
	.on("mouseout", function(d) {
        var c = viewModel.current();
        viewModel.pointed_at(c);
        viewModel.pointed_at_el(false);
    })
	.on("click", function(d) {
        if (!viewModel.is_current(d)) {
            viewModel.current(d.label);
            viewModel.current_el(this);
        }
    });
}


var dh = 250, dw = 1024;
var x0 = 10, x1 = 914;

var x = d3.scale.linear().domain([0,53]).range([x0, x1]),
    y = d3.scale.linear().domain([0,7]).range([20,dh]),

    r = d3.scale.linear().domain([0,1]).range([5,10]),
    r_med = d3.scale.linear().domain([0,1]).range([15,30]),
    r_big = d3.scale.linear().domain([0,1]).range([30, 43]),

    r_days_1 = d3.scale.linear().domain([0,1]).range([215, 225]),
    r_days_2 = d3.scale.linear().domain([0,1]).range([155, 175]),
    r_days_3 = d3.scale.linear().domain([0,1]).range([125, 145]),
    r_days_4 = d3.scale.linear().domain([0,1]).range([95, 115]),
    r_days_5 = d3.scale.linear().domain([0,1]).range([70, 90]),
    r_days_6 = d3.scale.linear().domain([0,1]).range([50, 70]),

    c0 = d3.scale.linear().domain([0,1]).range(
        ["hsl(250, 50%, 50%)", "hsl(350, 100%, 50%)"]
        ).interpolate(d3.interpolateHsl);
    c1 = d3.scale.linear().domain([0,1]).range(
        ["hsl(150, 50%, 50%)", "hsl(250, 100%, 50%)"]
        ).interpolate(d3.interpolateHsl);

var radii = {
    current: r,
    small: r,
    large: r_med,
    set_sizes: function(sm, lg) {
        radii.large = lg;
        radii.small = sm;
    },
};

var xm = d3.scale.linear().domain([0,7]).range([100, 814]),
    ym = d3.scale.linear().domain([0,4]).range([45, dh * 1.618]),
    xr = d3.scale.linear().domain([0,7]).range([0, 200]),
    yr = d3.scale.linear().domain([0,4]).range([45, dh * 1.618]);

var xmselector = d3.scale.linear().domain([1, 12]).range([x0, x1]);




function setup_month_tabs(V) {
    var months = ['January',
                  'February',
                  'March',
                  'April',
                  'May',
                  'June',
                  'July',
                  'August',
                  'September',
                  'October',
                  'November',
                  'December'];
    var R = _.range(12);
    var xscale = d3.scale.ordinal()
        .domain(R)
        .rangeBands([0, 900], 0.125);

    var mtabs = V.selectAll("g.mtab")
        .data(months);

    var mtabs_enter = mtabs.enter().append("svg:g")
        .attr("class", "mtab")
        .style("cursor", "pointer")
        .on("click", function(d, i) {
            viewModel.time_mode('m' + i)
        })
        .on("mouseover", function(d) {
    	    var it = d3.select(this)
    	    it.select("rect")
        	    .transition()
                .duration(200)
                .attr("height", 25)
                .attr("y", 80)
                .attr("ry", 5);
            it.select("text")
        	    .transition()
                .delay(100)
                .duration(200)
                .attr("fill-opacity", 0.5)
        })
        .on("mouseout", function(d) {
    	    var it = d3.select(this)
    	    it.select("rect")
         	    .transition()
                .delay(200)
                .duration(200)
                .attr("height", 5)
                .attr("y", 100)
                .attr("ry", 2);
            it.select("text")
        	    .transition()
                .duration(200)
                .attr("fill-opacity", 0)
        })
        ;

   var rects = mtabs_enter.append("svg:rect")
        .attr("x", function (d, i) { return xscale(i) })
        .attr("width", xscale.rangeBand())
        .attr("y", 100)
        .attr("height", 5)
        .attr("rx", 5)
        .attr("ry", 2)
        .attr("fill", function(d, i) {
            return (i % 2 == 0)
            ? c1(Math.random())
            : c0(Math.random()) })
        .attr("fill-opacity", 0)
        ;


       mtabs_enter.append("svg:text")
         .attr("x", function(d, i) { return xscale(i) + xscale.rangeBand() / 2 })
         .attr("y", 100)
         .attr("fill-opacity", 0)
         .attr("text-anchor", "middle")
         .text(function(d) { return "" + d; })
         ;

/*
         .attr("dx", -3) // padding-right
         .attr("dy", ".35em") // vertical-align: middle
         .attr("text-anchor", "end") // text-align: right
*/

    return rects;
}

function month_tabs_fade(V) {
    V.selectAll("g.mtab").remove();
}

function month_tabs_unfade(V) {
    setup_month_tabs(V)
        .transition()
        .delay(1200)
        .duration(500)
        .attr("fill-opacity", 0.5)
}


function select_date_range(from, to) {
    var style;
    var N = days_between(from, to);
    var in_range = function(d) {
        return (from <= d.date) && (d.date <= to);
    };
    var circles = vis3.selectAll("circle");
    if (N < 7) {
        style = daysish(N + 1);
        indexer = function (d, i) {
            d.selection_index = i;
            return d;
        }
    } else if (N <= 60) {
        style = monthsish;
        radii.set_sizes(r_med, r_med);
        indexer = function (d, i) {
            d.selection_index = d.month - month(from);
            console.log(d.selection_index)
            return d;
        }
    } else {
        style = year_style;
    }

    circles.filter(in_range)
    .map(indexer)
    .transition()
    .delay(function(d) { return 75 * Math.random() })
    .duration(function(d) { return 500 + (500 * Math.random()) })
    .call(style);
    clear_unmatching(circles, in_range, fade_drop);

}


function daysish(n) {
    console.log(n);
    var radius;
    var range;
    var margin = 0.125;
    switch (n) {
      case 1:
        radii.set_sizes(r_days_1, r_days_1);
        radius = r_days_1;
        range = [0, 900];
        break;
      case 2:
        radii.set_sizes(r_days_2, r_days_2);
        radius = r_days_2;
        range = [100, 800];
        margin = 1;
        break;
      case 3:
        radii.set_sizes(r_days_3, r_days_3);
        radius = r_days_3;
        range = [100, 800];
        margin = .35;
        break;
      case 4:
        radii.set_sizes(r_days_4, r_days_4);
        radius = r_days_4;
        range = [100, 800];
        break;
      case 5:
        radii.set_sizes(r_days_5, r_days_5);
        radius = r_days_5;
        range = [100, 800];
        break;
      case 6:
        radii.set_sizes(r_days_5, r_days_5);
        radius = r_days_6;
        range = [100, 800];
        break;
      default:
        radii.set_sizes(r_big, r_big);
        radius = r_big;
        range = [100, 800];
        margin = 0.125;
    }

    var xscale = d3.scale.ordinal()
        .domain(_.range(n))
        .rangePoints(range, margin);

    var f = function (T) { T
        .attr("cx", function(d) {
            return xscale(d.selection_index)
        })
        .attr("cy", dh)
        .attr("r", function() { return radius(Math.random()) })
        .call(shiny)
    }
    return f;
}

var xmh = d3.scale.linear().domain([0,7]).range([25, 300]);

function monthsish(T) { T
    .delay(function(d) { return 75 * Math.random() })
    .duration(function(d) { return 500 + (500 * Math.random()) })
    .attr("cx", function(d) { return 300 * d.selection_index + xmh(d.day_of_week) })
    .attr("cy", function(d) { return ym(d.week_of_month) })
    .attr("r", function() { return r_med(Math.random()) })
    .call(shiny)
}







//-------------------------------------------------------
// Arrange day-circles in various interesting patterns.
//

function select_year() {
    radii.large = r_med;
    radii.small = r;
    vis3.selectAll("circle")
        .transition()
        .delay(function(d) { return 230 * Math.random() })
        .duration(1200)
        .call(year_style);
 //   vis3.selectAll("text").transition().call(hidey);
}

function select_month(m) {
    radii.large = r_big;
    radii.small = r_big;
    var in_month = function(d) { return d.month == m };
    var circles = vis3.selectAll("circle");
    circles.filter(in_month).transition().call(month_style);
    clear_unmatching(circles, in_month, fade_drop);
/*
    var texts = vis3.selectAll("text")
    texts.filter(in_month).transition()
        .delay(600)
        .duration(300)
        .attr("x", function(d) { return xm(d.day_of_week) })
        .attr("y", function(d) { return ym(d.week_of_month) })
        .attr("fill-opacity", 1)
    clear_unmatching(texts, in_month, hidey);
*/
}

function select_week(w) {
    var in_week = function(d) { return d.week_of_year == w };
    var circles = vis3.selectAll("circle");

    circles.filter(in_week).transition().call(week_style);
    clear_unmatching(circles, in_week, fade_drop);
/*
    var texts = vis3.selectAll("text")
    texts.filter(in_week).transition()
        .duration(function(d) { return 500 + (500 * Math.random()) })
        .attr("x", function(d) { return xm(d.day_of_week) })
        .attr("y", function(d) { return ym(0) })
        .attr("fill-opacity", 1)
    clear_unmatching(texts, in_week, hidey);
*/
}

function select_day(day) {
    var in_day = function(d) { return d.day_of_year == day };
    clear_unmatching(
        vis3.selectAll("circle"),
        in_day,
        fade_drop);
}

function clear_unmatching(selection, predicate, effect) {
    selection.filter(function(d) { return !predicate(d) })
        .transition().call(effect);
}

//-------------------------------------------------------
// Effects bundles (used with .call(<effect>).)
//

function shiny(T) { T
    .attr("fill", function(d) {
        return (d.month % 2 == 0)
            ? c1(Math.random())
            : c0(Math.random());
    })
    .attr("fill-opacity", 0.5)
}

function hidey(T) { T
    .duration(300)
    .attr("fill-opacity", 0.01)
}

function fade_drop(T) { T
    .duration(1200)
    .attr("fill-opacity", 0.01)
  .transition()
    .delay(function(d) { return 680 * Math.random() })
    .attr("cx", function(d) { return x(d.week_of_year) })
    .attr("cy", h * 2)
    .ease("quad");
}

function embiggen(T) { T
    .attr("r", function(d) {
        return (viewModel.is_current(d))
            ? radii.current(Math.random())
            : radii.large(Math.random());
    })
    .duration(2500)
    .ease("elastic", 3, 0.3)
}

function shrink(T) { T
    .attr("r", function() { return radii.small(Math.random()) })
    .delay(100)
    .duration(333)
}

function swell(T) { T
    .attr("r", 2000)
    .delay(100)
    .duration(1333)
    .attr("fill-opacity", 0.01)
}

function week_style(T) { T
    .call(month_style)
    .attr("cy", function(d) { return ym(0) })
}

function month_style(T) { T
    .delay(function(d) { return 75 * Math.random() })
    .duration(function(d) { return 500 + (500 * Math.random()) })
    .attr("cx", function(d) { return xm(d.day_of_week) })
    .attr("cy", function(d) { return ym(d.week_of_month) })
    .attr("r", function() { return r_big(Math.random()) })
    .call(shiny)
}

function year_style(S) { S
    .attr("cx", function(d) { return x(d.week_of_year) })
    .attr("cy", function(d) { return 100 + y(d.day_of_week) })
    .attr("r", function() { return r(Math.random()) })
    .call(shiny)
}

function rangey_style(T) { T
    .delay(function(d) { return 75 * Math.random() })
    .duration(function(d) { return 500 + (500 * Math.random()) })
    .attr("cx", function(d) {
        return d.month * 200 + xr(d.day_of_week)
    })
    .attr("cy", function(d) { return yr(d.week_of_month) })
    .attr("r", function() { return r_big(Math.random()) })
    .call(shiny)
}


// Cribbed and modified from: http://www.mcfedries.com/javascript/daysbetween.asp
function days_between(date1, date2) {
    var date1_ms = date1.getTime()
    var date2_ms = date2.getTime()
    return Math.round(Math.abs(date1_ms - date2_ms) / 86400000)

}
