
var tile_widget = {
    id: "substitute_tiles",
    format: function(table) {
        var tiles = {};
        $(table).parents("#results").find(".tile").each(function() {
            var tile = $(this);
            tiles[tile.attr('index')] = tile;
            tile.detach()
        });
	    $("tbody tr", table).each(function() {
	        var row = $(this);
		    $("#results").append(tiles[row.attr('index')]);
		    row.hide();
	    });
    }

function make_tile(data, i) {
    $("div#results").append(

'<div id="tile_' + i + '" class="tile" index="' + i + '">' +

'<div id="desktop_tile_' + i + '" class="show-on-desktops row">' +
'  <div class="row"><div class="twelve columns">' +
'    <div class="three columns">' +
'        <div class="row"><div class="twelve columns"><div class="logo"><img src="/static/a_logo.png"></div></div></div>' +
'        <div class="row"><div class="twelve columns"><div class="spa">' + data.spa + '</div></div></div>' +
'    </div>' +
'    <div class="six columns">' +
'        <div class="row"><div class="twelve columns"><div class="rating">Rating: ' + data.rating + '</div></div></div>' +
'        <div class="row"><div class="twelve columns"><div class="distance" distance="' + data.distance + '">Distance: ' + data.distance_text + '</div></div></div>' +
'    </div>' +
'    <div class="three columns">' +
'        <div class="price">$' + data.price + '</div>' +
'    </div>' +
'  </div></div>' +
'  <div class="row"><div class="twelve columns">' +
'        <div class="details">All kinds of info about ' + data.spa + '!</div>' +
'  </div></div>' +
'</div>' +

'<div id="mobile_tile_' + i + '" class="show-on-phones row">' +
'    <div class="six columns centered">' +
'        <div class="logo"><img src="/static/a_logo.png"></div>' +
'        <div class="row"><div class="twelve columns"><div class="spa">' + data.spa + '</div></div></div>' +
'        <div class="row"><div class="twelve columns"><div class="rating">Rating: ' + data.rating + '</div></div></div>' +
'        <div class="row"><div class="twelve columns"><div class="distance" distance="' + data.distance + '">Distance: ' + data.distance_text + '</div></div></div>' +
'        <div class="row"><div class="twelve columns"><div class="rice">$' + data.price + '</div></div></div>' +
'    </div>' +
'</div>' +

'</div>');

    $("#desktop_tile_" + i).hover(
      function () { $(this).find('.details').slideDown() },
      function () { $(this).find('.details').slideUp() }
    );

    $("#desktop_tile_" + i).find('.details').slideUp(1);

    $("table#resultsTable tbody").append(
'<tr id="trow_' + i + '" index="' + i + '" >' +
'  <td>' + data.spa + '</td>' +
'  <td>' + data.rating + '</td>' +
'  <td><span distance="' + data.distance + '">' + data.distance_text + '</span></td>' +
'  <td>$' + data.price + '</td>' +
'</tr>');

}

/*
    jQuery.map(foo, make_tile);

    $("#resultsTable").tablesorter({
        widgets: ['substitute_tiles']
    });
*/


				<div id="results">
					<table id="resultsTable" class="tablesorter">
					<thead>
						<tr>
							<th>Spa</th>
							<th>Rating</th>
							<th>Distance</th>
							<th>Price</th>
						</tr>
					</thead>
					<tbody>
					</tbody>
					</table>
				</div>{# "results" #}

