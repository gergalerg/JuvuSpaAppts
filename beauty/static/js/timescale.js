
var h = 714, w = 1024;
var y0 = 10, y1 = 914;

var left = 20, right = 645;
var slider_offset = 0.0;

var hour = d3.time.format("%H:%M");

var early = new Date(2011, 0, 1, 5);
var night = new Date(2011, 0, 1, 21, 1);

var day_to_n = d3.time.scale()
    .domain([early, night])
    .range([0, 1])

var n_to_y = d3.scale.linear()
    .domain([0, 0.25, 0.75, 1])
    .range([10, 110, 610, 710])

function day_line(d) {
    return n_to_y(day_to_n(d) + slider_offset) - 400 * slider_offset;
}

var ticks = day_to_n.ticks(d3.time.minutes, 15);
var m = 4; // Special format every mth line to highlight hour.

function make_timescale(svg_el) {
    svg_el.selectAll("line")
        .data(ticks)
      .enter().append("svg:line")
//        .attr("x1", function(d, i) { return left + ((i % m == 0) ? 50 : 54 )})
        .attr("x1", left + 50)
        .attr("x2", function(d, i) { return left + ((i % m == 0) ? right : (right - 12) )})
        .attr("y1", day_line)
        .attr("y2", day_line)
        .attr("stroke", function(d, i) { return (i % m == 0) ? "#787D78" : "#ccc" })
        .attr("stroke-dasharray", function(d, i) { return (i % m == 0) ? "" : "2,1" })
        .on("mouseover", function(d) {
            viewModel.mouse_time(hour(d));
        });

    svg_el.selectAll("text.date_rule")
        .data(ticks)
    .enter().append("svg:text")
        .filter(function(d, i) { return i % m == 0 })
        .attr("text-anchor", "end")
        .attr("class", "date_rule")
        .attr("x", left + 45)
        .attr("y", day_line)
        .attr("dy", 4)
        .text(hour)
}

var timescale_updater = _.throttle(function() {
    d3.selectAll("line")
        .transition()
        .delay(0)
        .duration(50)
        .attr("y1", day_line)
        .attr("y2", day_line);
    d3.selectAll("text.date_rule")
        .transition()
        .delay(0)
        .duration(50)
        .attr("y", day_line);
    d3.selectAll("rect")
        .transition()
        .delay(0)
        .duration(50)
        .attr("y", function(d) { return day_line(d.start) })
        .attr("height", function(d) { return day_line(d.end) - day_line(d.start) });
}, 50);

