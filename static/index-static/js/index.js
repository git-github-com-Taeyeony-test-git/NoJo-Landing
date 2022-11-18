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
    let password = $("#comment-password").val();
    let comment = $("#comment").val();
    $.ajax({
        type: "POST",
        url: "/api/index/comment",
        data: { name_give: name, password_give: password, comment_give: comment },
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
        url: "/api/index/comment/delete",
        data: { num_give: num, password_give: password_input },
        success: function (response) {
            alert(response["msg"])
            window.location.reload();
        }
    })

}

function comment_modify(num) {
    var password_input = prompt('비밀번호를 입력하세요', '비밀번호');

    // 수정된 코멘트 들고오기
    let comment = $("#modify").val()

    $.ajax({
        type: "POST",
        url: "/api/index/comment/modify",
        data: { num_give: num, password_give: password_input, comment_give: comment },
        success: function (response) {
            alert(response["msg"])
            window.location.reload();
        }
    })
}

function comment_modify_form(num, comment) {

    let temp_html = `
        <textarea
            class="comment-text-input"
            name="comment"
            id="modify"
            cols="30"
            rows="5"
            placeholder="내용"
            
        >${comment}</textarea>
        <div class="comment-btn-wrap">
            <button class="comment-btn" onclick="comment_modify(${num})">
                수정
            </button>
        </div>
    `

    $('.comment-list-data[' + "data-index=" + '"' + num + '"' + '] .test').remove();
    $('.comment-list-data[' + "data-index=" + '"' + num + '"' + '] .comment-list-data-btn-wrap').remove();
    $('.comment-list-data[' + "data-index=" + '"' + num + '"' + '] .comment-list-data-content').append(temp_html);

}

function show_comment() {
    $.ajax({
        type: "GET",
        url: "/api/index/comment",
        data: {},
        success: function (response) {
            let rows = response["comments"];

            console.log(typeof (rows))

            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name'];
                let comment = rows[i]['comment'];
                let password = rows[i]['password'];
                let num = rows[i]['num'];

                // console.log(comment);
                let temp_html = `
                    <div class="comment-list-data" data-index=${num}>
                        <div class="comment-list-data-name">${name}</div>
                        <div class="comment-list-data-content"><div class="test">${comment}</div></div>
                        <div class="comment-list-data-btn-wrap">
                            <button id="comment-modify" class="comment-list-data-btn-modify" onclick="comment_modify_form(${num}, '${comment}')" >수정</button>
                            <button class="comment-list-data-btn-delete" onclick="comment_delete(${num})">삭제</button>
                        </div>
                    </div>
                `;

                $("#comment-list-data-wrap").append(temp_html);
            }
        }
    })
}