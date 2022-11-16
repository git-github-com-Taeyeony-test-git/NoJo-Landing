$(document).ready(function () {
    show_comment();
    let isOpen = false;
    $(".arrow-button").on("click", function () {
        if (isOpen == false) {
            $(".member-card-back").fadeIn(500);
            isOpen = true;
        } else {
            $(".member-card-back").fadeOut(500);
            isOpen = false;
        }

        let offset = $(".member-card-back").offset();
        $("html, body").animate({ scrollTop: offset.top }, 1000);
    });
});

function save_comment() {
    let name = $("#comment-name").val();
    let comment = $("#comment").val();
    $.ajax({
        type: "POST",
        url: "/api/JungMin/comment",
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
        url: "/api/JungMin/comment",
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
