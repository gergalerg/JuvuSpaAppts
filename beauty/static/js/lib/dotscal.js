//-------------------------------------------------------
// Date Formatting and Scales.
//

var day = d3.time.format("%w"),
    week = d3.time.format("%U"),
    _month = d3.time.format("%m"),
    mday = d3.time.format("%d"),
    yday = d3.time.format("%j"),
    format = d3.time.format("%A, %B %d %Y");

function month(d) { return _month(d) - 1 }

var dh = 250, w = 1024;
var x0 = 10, x1 = 914;

var x = d3.scale.linear().domain([0,53]).range([x0, x1]),
    y = d3.scale.linear().domain([0,7]).range([20,dh]),

    r = d3.scale.linear().domain([0,1]).range([5,10]),
    r_med = d3.scale.linear().domain([0,1]).range([15,30]),
    r_big = d3.scale.linear().domain([0,1]).range([30, 43]),

    c0 = d3.scale.linear().domain([0,1]).range(
        ["hsl(250, 50%, 50%)", "hsl(350, 100%, 50%)"]
        ).interpolate(d3.interpolateHsl);
    c1 = d3.scale.linear().domain([0,1]).range(
        ["hsl(150, 50%, 50%)", "hsl(250, 100%, 50%)"]
        ).interpolate(d3.interpolateHsl);

var xm = d3.scale.linear().domain([0,7]).range([100, 814]),
    ym = d3.scale.linear().domain([0,4]).range([45, dh * 1.618]);

var xmselector = d3.scale.linear().domain([1, 12]).range([x0, x1]);

//-------------------------------------------------------
// Arrange day-circles in various interesting patterns.
//

function select_year() {
    d3.selectAll("circle")
        .transition()
        .delay(function(d) { return 230 * Math.random() })
        .duration(1200)
        .call(year_style);
    d3.selectAll("text").transition().call(hidey);
}

function select_month(m) {
    var in_month = function(d) { return d.month == m };
    var circles = d3.selectAll("circle");
    circles.filter(in_month).transition().call(month_style);
    clear_unmatching(circles, in_month, fade_drop);

    var texts = d3.selectAll("text")
    texts.filter(in_month).transition()
        .delay(600)
        .duration(300)
        .attr("x", function(d) { return xm(d.day_of_week) })
        .attr("y", function(d) { return ym(d.week_of_month) })
        .attr("fill-opacity", 1)
    clear_unmatching(texts, in_month, hidey);
}

function select_week(w) {
    var in_week = function(d) { return d.week_of_year == w };
    var circles = d3.selectAll("circle");

    circles.filter(in_week).transition().call(week_style);
    clear_unmatching(circles, in_week, fade_drop);

    var texts = d3.selectAll("text")
    texts.filter(in_week).transition()
        .duration(function(d) { return 500 + (500 * Math.random()) })
        .attr("x", function(d) { return xm(d.day_of_week) })
        .attr("y", function(d) { return ym(0) })
        .attr("fill-opacity", 1)
    clear_unmatching(texts, in_week, hidey);
}

function select_day(day) {
    var in_day = function(d) { return d.day_of_year == day };
    clear_unmatching(
        d3.selectAll("circle"),
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
            ? r_big(Math.random())
            : (viewModel.viewing() == "year")
                ? r_med(Math.random())
                : r_big(Math.random());
    })
    .duration(2500)
    .ease("elastic", 3, 0.3)
}

function shrink(T) { T
    .attr("r", function() {
        return (viewModel.viewing() == "year")
            ? r(Math.random())
            :  r_big(Math.random())
    })
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
    .attr("cy", function(d) { return y(d.day_of_week) })
    .attr("r", function() { return r(Math.random()) })
    .call(shiny)
}


