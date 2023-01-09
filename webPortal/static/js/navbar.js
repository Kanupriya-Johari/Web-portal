$('#navigation_2_dropdown_1').on("click", function () {
    $('.dropdown-menu').toggleClass("active");
});

$('.dropdown-menu div div').on('click', function () {
    $('#navigation_2_dropdown_1').text($(this).text());
    $('.dropdown-menu').toggleClass("active");
})