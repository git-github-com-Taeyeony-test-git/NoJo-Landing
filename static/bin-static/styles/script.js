$(document).ready(function () {
    show_comment();

    let isOpen = false;
    $(".arrow-button").on("click", function () {
        if (isOpen == false) {
            $(".member-card-back").fadeIn(500);
            document.getElementById('profile_onoff').innerHTML = '소개닫기'
            isOpen = true;
        } else {
            $(".member-card-back").fadeOut(500);
            document.getElementById('profile_onoff').innerHTML = '소개보기'
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
        url: "/api/bin/comment",
        data: { name_give: name, comment_give: comment },
        success: function (response) {
            alert(response["msg"])
            window.location.reload();
        }
    })
}

function comment_delete(num) {
    var password_input = prompt('비밀번호를 입력하세요', '비밀번호');
    $.ajax({
        type: "POST",
        url: "/api/bin/comment/delete",
        data: { num_give: num, password_give: password_input },
        success: function (response) {
            alert(response["msg"])
            window.location.reload();
        }
    })

}

function show_comment() {
    $.ajax({
        type: "GET",
        url: "/api/bin/comment",
        data: {},
        success: function (response) {
            let rows = response["comments"];

            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name'];
                let comment = rows[i]['comment'];
                let password = rows[i]['password'];
                let num = rows[i]['num'];

                let temp_html = `
                    <div class="comment-list-data" data-index=${num}>
                        <div class="comment-list-data-name">${name}</div>
                        <div class="comment-list-data-content"><div class="test">${comment}</div></div>
                        <div class="comment-list-data-btn-wrap">
                            <button class="comment-list-data-btn-delete" onclick="comment_delete(${num})">삭제</button>
                        </div>
                    </div>
                `;

                $("#comment-list-data-wrap").append(temp_html);
            }
        }
    })
}