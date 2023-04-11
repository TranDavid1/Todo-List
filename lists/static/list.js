var initialize = function () {
    // find any input elements whose name attribute is "text"
    // add an event listener to react on keypress events
    $('input[name="text"]').on("keypress", function () {
        $(".has-error").hide();
    });
};
