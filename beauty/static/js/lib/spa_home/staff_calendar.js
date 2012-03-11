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


//-------------------------------------------------------
// Staff member calendar view support.
//

var color_of = d3.scale.linear()
        .domain([0, 1])
        .range(["hsl(0, 50%, 70%)", "hsl(360, 50%, 70%)"])
        .interpolate(d3.interpolateHsl);

function setup_bands() {
    var R = _.range(viewModel.staff().length);
    var x = d3.scale.ordinal()
        .domain(R)
        .rangeBands([80, 335], 0.125);
    var col = d3.scale.ordinal()
        .domain(R)
        .rangePoints([0.0, 1.0], 0.5);

    _.each(viewModel.staff(), function(n, i) {
        n.tag_color(color_of(col(i)));
    });

    var Apointments = _.flatten(_.map(viewModel.staff(), random_apts));

    d3.select("svg")
      .selectAll("rect")
      .remove();

    d3.select("svg")
      .selectAll("rect")
      .data(Apointments)
      .enter().append("svg:rect")
        .attr("x", function(d) { return x(_.indexOf(viewModel.staff(), d.staff_member)) })
        .attr("width", x.rangeBand())
        .attr("y", function(d) { return day_line(d.start) })
        .attr("height", function(d) { return day_line(d.end) - day_line(d.start) })
        .attr("fill", function(d) { return d.staff_member.tag_color() })
        .on("mouseover", function(d) {
            viewModel.mouse_time(hour(d.start));
        });
}

