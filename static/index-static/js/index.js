$(document).ready(function () {

    var num = 2

    $('#page-btn').on('click', function () {

        if (num == 4) {
            $('html,body').animate({ scrollTop: $(`#section-1`).offset().top - 110 }, 'slow');
            num = 2
        } else {
            $('html,body').animate({ scrollTop: $(`#section-${num}`).offset().top - 110 }, 'slow');
            num = num + 1
        }
    })
})