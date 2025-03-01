$('#filter_form').on('change', 'input, select', function () {
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