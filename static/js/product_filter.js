$('#filter_form').on('keyup change paste', 'input, select', function () {
    console.log("AAA");
    $.ajax({
        url: product_filter_url,
        data: $('#filter_form').serialize(),
        method: 'GET',
        success: function (r) {
            $('#product_list').html(r);
        },
        error: function (r) {
        },
        complete: function (r) {
        },
    });
});

$('.pheight_select').change(function () {
    if ($(this).val() == 'other') {
        $('#other_pheight').show();
    } else {
        $('#other_pheight').hide();
    }
});