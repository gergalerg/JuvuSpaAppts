
var choose_view_transitions = {

    dis: function() {
        options_transitions.clickDis();
        if (viewModel.first_choose) {
            options_transitions.little_show_nei();
            viewModel.first_choose = false;
        }
    },

    nei: function() {
        options_transitions.clickNei();
        if (viewModel.first_choose) {
            options_transitions.little_show_dis();
            viewModel.first_choose = false;
        }
    },

    date: function() { options_transitions.clickDate(); },

    opts: function() { options_transitions.clickOpts(); }
};

var choose_unview_transitions = {

    dis: function() {
        if (viewModel.current_filter() == 'nei') {
            options_transitions.little_show_dis();
        } else {
            options_transitions.hide_dis();
        }
    },

    nei: function() {
        if (viewModel.current_filter() == 'dis') {
            options_transitions.little_show_nei();
        } else {
            options_transitions.hide_nei();
        }
    },

    date: function() { options_transitions.hide_when(); },

    opts: function() { options_transitions.hide_opts(); }
};

function choose_unview() {
    var old_filter = viewModel.previous_filter;
    viewModel.previous_filter = viewModel.current_filter();
    if (old_filter == '') {
        return;
    }
    if (!_.has(choose_unview_transitions, old_filter)) {
        console.log('unknown choose_unview', old_filter);
        return;
    }
    console.log('choose_unviewing', old_filter);
    var f = choose_unview_transitions[old_filter];
    f();
}

viewModel.current_filter.subscribe(function(filter) {
    console.log('choose_viewing', filter);
    choose_unview();
    if (!_.has(choose_view_transitions, filter)) {
        console.log('unknown filter', filter);
        routes.navigate('toc', true);
        return;
    }
    var f = choose_view_transitions[filter];
    f();
});

var reveal_when_circles = _.once(function() {
  d3.select('.c_to').transition()
    .attr('r', 65)
    .attr('fill-opacity', 1)
    .duration(500);

  d3.select('.c_date').transition()
    .attr('r', 65)
    .attr('fill-opacity', 1)
    .duration(500);

  d3.select('.today').transition()
    .style('display', 'block')
    .style('opacity', '1')
    .duration(500);

  d3.select('.date').transition()
    .style('display', 'block')
    .style('opacity', '1')
    .duration(500);
});

var reveal_option_circle = _.once(function() {
  d3.select('.c_op').transition()
    .attr('cx', 800)
    .attr('cy', 350)
    .attr('r', 65)
    .attr('fill-opacity', 1)
    .duration(500);

  d3.select('.c_me').transition()
    .attr('r', 65)
    .attr('fill-opacity', 1)
    .duration(500);

  d3.select('.option').transition()
    .style('left', '625px')
    .style('top', '345px')
    .style('display', 'block')
    .style('opacity', '1')
    .duration(500);

  d3.select('.op_list').transition()
    .style('display', 'none')
    .style('opacity', '0');

  d3.select('.juvuMe').transition()
    .style('display', 'block')
    .style('opacity', '1')
    .duration(500);
});

var options_transitions = {

    clickDis: function() {
        $('.c_dis').appendTo($('.s_canvas'));
      d3.select('.c_dis').transition()
        .attr('cx', 400)
        .attr('cy', 230)
        .attr('r', 200)
        .attr('fill', first_color)
        .duration(1000)
        .ease('elastic', 5, 3);

      d3.select('.distance').transition()
        .style('left', '255px')
        .style('top', '170px')
        .duration(1000)
        .ease('elastic', 5, 3)
          .transition()
        .style('display', 'block')
        .style('opacity', 1)
        .delay(1000)
        .duration(300);

      d3.select('.dis_form').transition()
        .style('display', 'block')
        .style('opacity', '1')
        .duration(500)
        .delay(500);

      d3.select('.where').transition()
        .style('display', 'none')
        .style('opacity', 0);
  },

  hide_dis: function() {
    d3.select('.c_dis').transition()
        .attr('cx', 100)
        .attr('cy', 100)
        .attr('r', 0)
        .attr('fill', 'steelblue')
        .duration(500)
        .ease('elastic', 5, 4)
        .transition()
        .attr('r', 30)
        .delay(500)
        .duration(1000)
        .ease('elastic', 5, 4);

    d3.select('.distance').transition()
        .style('display', 'none')
        .style('opacity', 0);

    d3.select('.c_nei').transition()
        .attr('cx', 595)
        .attr('cy', 300)
        .attr('r', 0)
        .duration(1000)
        .ease('elastic', 5, 4);

      d3.select('.neighbor').transition()
        .style('display', 'none')
        .style('opacity', '0');

      d3.select('.where').transition()
        .style('display', 'block')
        .style('opacity', 1)
        .delay(1000)
       .duration(100);
  },

  little_show_dis: function() {
      d3.select('.c_dis').transition()
        .attr('cx', 305)
        .attr('cy', 110)
        .attr('r', 65)
        .duration(1000)
        .ease('elastic', 5, 4);

      d3.select('.distance').transition()
        .style('display', 'block')
        .style('left', '155px')
        .style('top', '105px')
        .duration(1000)
        .ease('elastic', 5, 4)
        .transition()
        .style('display', 'block')
        .style('opacity', '1')
        .delay(1000)
        .duration(300);

      d3.select('.dis_form').transition()
        .style('display', 'none')
        .style('opacity', '0')
        .duration(500);
  },

  little_show_nei: function() {
      d3.select('.c_nei').transition()
        .attr('cx', 615)
        .attr('cy', 410)
        .attr('r', 65)
        .duration(1000)
        .ease('elastic', 5, 4);

      d3.select('.neighbor').transition()
        .style('left', ' 442px')
        .style('top', ' 400px')
        .style('display', 'none')
        .style('opacity', 0)
        .duration(1000)
        .ease('elastic', 5, 4)
          .transition()
        .style('display', 'block')
        .style('opacity', '1')
        .delay(1000)
        .duration(300);

      d3.select('.nei_form').transition()
        .style('display', 'none')
        .style('opacity', '0')
        .duration(500);
  },

  clickNei: function() {

        $('.c_nei').appendTo($('.s_canvas'));
      d3.select('.c_nei').transition()
        .attr('cx', 500)
        .attr('cy', 300)
        .attr('r', 235)
        .attr('fill', second_color)
        .duration(1000)
        .ease('elastic', 5, 4);

      d3.select('.neighbor').transition()
        .style('left', ' 327px')
        .style('top', ' 170px')
        .duration(1000)
        .ease('elastic', 5, 4);

      d3.select('.nei_form').transition()
        .style('display', 'block')
        .style('opacity', '1')
        .duration(500)
        .delay(500);

      d3.select('.neighbor').transition()
        .style('display', 'block')
        .style('opacity', 1)
        .delay(1000)
        .duration(300);

      d3.select('.where').transition()
        .style('display', 'none')
        .style('opacity', 0);
  },

  hide_nei: function() {
    d3.select('.c_nei').transition()
        .attr('cx', 100)
        .attr('cy', 100)
        .attr('r', 0)
        .attr('fill', 'steelblue')
        .duration(500)
        .ease('elastic', 5, 4)
        .transition()
        .attr('r', 30)
        .delay(500)
        .duration(1000)
        .ease('elastic', 5, 4);

      d3.select('.neighbor').transition()
        .style('display', 'none')
        .style('opacity', 0);

    d3.select('.c_dis').transition()
        .attr('cx', 450)
        .attr('cy', 170)
        .attr('r', 0)
        .duration(1000)
        .ease('elastic', 5, 4);

    d3.select('.distance').transition()
        .style('display', 'none')
        .style('opacity', '0');

      d3.select('.where').transition()
        .style('display', 'block')
        .style('opacity', 1)
        .delay(1000)
       .duration(100);
  },

  clickDate: function() {
    d3.select('.c_date').transition()
      .attr('cx', 550)
      .attr('cy', 400)
      .attr('r', 150)
      .attr('fill', second_color)
      .duration(1000)
      .ease('elastic', 5, 4);

    d3.select('.c_to').transition()
      .attr('cx', 425)
      .attr('cy', 255)
      .attr('r', 65)
      .duration(1000)
      .ease('elastic', 5, 4);

    d3.select('.date').transition()
      .style('left', '400px')
      .style('top', '345px')
      .transition()
      .style('display', 'block')
      .style('opacity', '1')
      .duration(1000)
      .delay(1000)
      .ease('elastic', 5, 4);

    d3.select('.today').transition()
      .style('left', '405px')
      .style('top', '250px')
      .transition()
      .style('display', 'block')
      .style('opacity', '1')
      .duration(1000)
      .delay(1000)
      .ease('elastic', 5, 4);

    d3.select('.date_form').transition()
      .style('display', 'block')
      .style('opacity', '1')
      .duration(1000)
      .delay(1000)
      .ease('elastic', 5, 4);

    d3.select('.when').transition()
      .style('display', 'none')
      .style('opacity', 0);
  },

  hide_when: function() {
    d3.select('.c_to').transition()
      .attr('cx', 100)
      .attr('cy', 200)
      .attr('r', 0)
      .duration(500)
        .ease('elastic', 5, 4);

      d3.select('.c_date').transition()
        .attr('cx', 100)
      .attr('cy', 200)
        .attr('r', 0)
        .attr('fill', 'steelblue')
        .duration(500)
        .ease('elastic', 5, 4)
        .transition()
        .attr('r', 30)
        .style('display', 'block')
        .style('opacity', 1)
        .delay(500)
        .duration(1000)
        .ease('elastic', 5, 4);

      d3.select('.today').transition()
        .style('display', 'none')
        .style('opacity', 0);

      d3.select('.date').transition()
        .style('display', 'none')
        .style('opacity', '0');

      d3.select('.when').transition()
        .style('display', 'block')
        .style('opacity', 1)
        .delay(1000)
       .duration(100);
  },

  clickOpts: function() {
    d3.select('.c_op').transition()
      .attr('cx', 500)
      .attr('cy', 300)
      .attr('r', 180)
      .attr('fill', first_color)
      .attr('fill-opacity', 1)
      .duration(500);

    d3.select('.option').transition()
      .style('left', '325px')
      .style('top', '190px')
      .style('display', 'block')
      .style('color', second_color)
      .style('opacity', '1')
      .duration(500);

    d3.select('.op_list').transition()
      .style('display', 'block')
      .style('opacity', '1')
      .duration(500)
      .delay(500);
  },

  hide_opts: function() {
    d3.select('.c_op').transition()
      .attr('cx', 100)
        .attr('cy', 300)
        .attr('r', 0)
        .attr('fill', 'steelblue')
        .duration(500)
        .ease('elastic', 5, 4)
      .transition()
      .attr('r', 30)
        .delay(500)
        .duration(1000)
        .ease('elastic', 5, 4);

      d3.select('.option').transition()
      .style('left', '-75px')
      .style('top', '293px')
      .style('color', 'white')
      .style('display', 'none')
      .transition()
      .style('display', 'block')
      .style('opacity', '1')
      .delay(500)
      .duration(500);

      d3.select('.op_list').transition()
      .style('display', 'none')
      .style('opacity', '0')
      .duration(500);
  }
};



//###########################################################################

        function click_dateBtn()
        {
          d3.select('.c_date').transition()
            .attr('cx', 100)
            .attr('cy', 200)
            .attr('r', 0)
            .attr('fill', 'steelblue')
            .duration(500)
              .ease('elastic', 5, 4);

            d3.select('.c_date').transition()
              .attr('r', 30)
              .delay(500)
              .duration(1000)
              .ease('elastic', 5, 4);

            d3.select('.c_to').transition()
              .attr('r', 0)
              .duration(1000)
              .ease('elastic', 5, 4);

            d3.select('.today').transition()
              .style('display', 'none')
              .style('opacity', 0);

            d3.select('.date').transition()
              .style('display', 'none')
              .style('opacity', '0');

            d3.select('.when').transition()
              .style('display', 'block')
              .style('opacity', 1)
           .duration(100);
        }

        function runDate()
        {
          d3.select('.c_to').transition()
            .attr('cx', 100)
            .attr('cy', 200)
            .attr('r', 0)
            .duration(500)
              .ease('elastic', 5, 4);

            d3.select('.c_date').transition()
              .attr('cx', 100)
            .attr('cy', 200)
              .attr('r', 0)
              .attr('fill', 'steelblue')
              .duration(500)
              .ease('elastic', 5, 4);

            d3.select('.c_date').transition()
              .attr('r', 30)
              .style('display', 'block')
              .style('opacity', 1)
              .delay(500)
              .duration(1000)
              .ease('elastic', 5, 4);

            d3.select('.date').transition()
              .style('display', 'none')
              .style('opacity', '0');

            d3.select('.today').transition()
              .style('display', 'none')
              .style('opacity', 0);

            d3.select('.when').transition()
              .style('display', 'block')
              .style('opacity', 1)
              .delay(1000)
           .duration(100);
        }

