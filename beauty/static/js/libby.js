
function setup_button(sel, ico) {
    $(sel).button({icons: {primary:ico}, text: false })
        .click(function(){return false});
}

