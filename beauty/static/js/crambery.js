//-------------------------------------------------------
// Animate color cycle.
//

var cram_color = d3.scale.linear().domain([0,11]).range(
        ["hsl(0, 50%, 90%)", "hsl(360, 50%, 90%)"]
        ).interpolate(d3.interpolateHsl);

function crambery(minutes) {
    window.setTimeout(crambery, 60000 * minutes, minutes);
    for (var i = 0; i < 12; i++) {
        d3.select("body").transition()
            .delay(minutes * 5000 * i)
            .duration(minutes * 5000)
            .style("background-color", cram_color(i));
    }
}


