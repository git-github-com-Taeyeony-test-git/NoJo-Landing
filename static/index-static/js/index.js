$(document).ready(function () {

    show_comment();

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
});

function save_comment() {
    let name = $("#comment-name").val();
    let comment = $("#comment").val();
    $.ajax({
        type: "POST",
        url: "/api/index/comment",
        data: { name_give: name, comment_give: comment },
        success: function (response) {
            alert(response["msg"])
            window.location.reload();
        }
    })
}

function show_comment() {
    $.ajax({
        type: "GET",
        url: "/api/index/comment",
        data: {},
        success: function (response) {
            let rows = response["comments"];

            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name'];
                let comment = rows[i]['comment'];

                let temp_html = `
                    <div class="comment-list-data">
                        <div class="comment-list-data-name">${name}</div>
                        <div class="comment-list-data-content">${comment}</div>
                    </div>
                `;

                $("#comment-list-data-wrap").append(temp_html);
            }
        }
    })
}