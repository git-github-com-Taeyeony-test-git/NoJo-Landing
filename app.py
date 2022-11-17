from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.c4jurvw.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/asher")
def asher():
    return render_template("asher-landing.html")

@app.route("/JungMin")
def JungMin():
    return render_template('Jungmin.html')

@app.route("/bin")
def bin():
    return render_template("bin.html")

@app.route("/Taeyeon")
def Taeyeon():
    return render_template("Taeyeon.html")

@app.route("/jiyoung")
def jiyoung():
    return render_template("jiyoung.html")

# index api
@app.route("/api/index/comment", methods=["POST"])
def index_comment_post():
    name_receive = request.form['name_give']
    password_receive = request.form['password_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.index_comment.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'password': password_receive,
        'comment': comment_receive
    }

    db.index_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/index/comment", methods=["GET"])
def index_comment_get():

    comment_list = list(db.index_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route("/api/index/comment/delete", methods=["POST"])
def index_comment_delete(): 
    # 글 번호
    num_receive = request.form['num_give']
    # 입력받아 넘긴 비밀번호
    password_receive = request.form['password_give']

    # db에서 가져온 비밀번호
    password_db = db.index_comment.find_one({'num': int(num_receive)}, {'_id': False});
    password = password_db['password'];

    # 비밀번호 체크 : 실패하면 메시지리턴
    if (password_receive != password) :
        return jsonify({'msg': '삭제 실패'})

    db.index_comment.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제성공'})

@app.route("/api/index/comment/modify", methods=["POST"])
def index_comment_modify():
    # 글 번호
    num_receive = request.form['num_give']
    # 입력받아 넘긴 비밀번호
    password_receive = request.form['password_give']
    # 수정된 내용
    comment_receive = request.form['comment_give']

    # db에서 가져온 비밀번호
    password_db = db.index_comment.find_one({'num': int(num_receive)}, {'_id': False});
    password = password_db['password'];

    # 비밀번호 체크 : 실패하면 메시지리턴
    if (password_receive != password) :
        return jsonify({'msg': '수정 실패'})

    db.index_comment.update_one({'num': int(num_receive)}, {'$set': {'comment': comment_receive}})
    return jsonify({'msg': '수정성공'})

     

# asher api
@app.route("/api/asher/intro", methods=["GET"])
def asher_intro_get():

    intro_list = list(db.member_intro.find({'name': '박현민'}, {'_id': False}))
    return jsonify({'intros': intro_list})


@app.route("/api/asher/comment", methods=["POST"])
def asher_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.asher_comment.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive
    }

    db.asher_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/asher/comment", methods=["GET"])
def asher_comment_get():

    comment_list = list(db.asher_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route("/api/asher/comment/delete", methods=["POST"])
def asher_comment_delete(): 
    # 글 번호
    num_receive = request.form['num_give']

    db.asher_comment.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제성공'})


# bin api
@app.route("/api/bin/comment", methods=["POST"])
def bin_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    password_receive = request.form['password_give']

    comment_list = list(db.bin_comment.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive,
        'password': password_receive
    }

    db.bin_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/bin/comment", methods=["GET"])
def bin_comment_get():
    
    comment_list = list(db.bin_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

# bin comment
@app.route("/api/bin/comment/delete", methods=["POST"])
def bin_index_comment_delete(): 
    # 글 번호
    num_receive = request.form['num_give']
    # 입력받아 넘긴 비밀번호
    password_receive = request.form['password_give']

    # db에서 가져온 비밀번호
    password_db = db.bin_comment.find_one({'num': int(num_receive)}, {'_id': False});
    password = password_db['password'];

    admin_db = db.bin_comment.find_one({'num': int(0)}, {'_id': False});
    admin_pw_db = admin_db['admin_db'];

    # 비밀번호 체크 : 실패하면 메시지리턴
    if (password_receive == password) :
        # return jsonify({'msg': '삭제 실패'})
        db.bin_comment.delete_one({'num': int(num_receive)})
        return jsonify({'msg': '삭제성공'})
    elif (password_receive == admin_pw_db) :
        db.bin_comment.delete_one({'num': int(num_receive)})
        return jsonify({'msg': '주인장 권한으로 삭제성공'})
    else :
        return jsonify({'msg': '삭제 실패'})


# JungMin api
@app.route("/api/JungMin/comment", methods=["POST"])
def JungMin_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    num_list = list(db.JungMin_comment.find({},{'_id':False}))
    count = len(num_list) + 1

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'num': count
    }

    db.JungMin_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/JungMin/comment", methods=["GET"])
def jungmin_comment_get():
    
    comment_list = list(db.JungMin_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})
    
@app.route("/api/JungMin/comment/delete", methods=["POST"])
def jungmin_comment_delet():
    num_receive = request.form['num_give']
    db.JungMin_comment.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제성공'})

# Taeyeon api
@app.route("/api/Taeyeon/comment", methods=["POST"])
def Taeyeon_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.Taeyeon_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/Taeyeon/comment", methods=["GET"])
def Taeyeon_comment_get():
    
    comment_list = list(db.Taeyeon_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

# jiyoung api
@app.route("/api/jiyoung/comment", methods=["POST"])
def jiyoung_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.jiyoung_comment.find({}, {'_id': False}))
    count=len(comment_list)+1

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'num' : count
    }

    db.jiyoung_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/jiyoung/comment", methods=["GET"])
def jiyoung_comment_get():
    
    comment_list = list(db.jiyoung_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route("/api/jiyoung/comment/delete", methods=["POST"])
def jiyoung_comment_delete():
    # 글 번호
    num_receive = request.form['num_give']

    db.jiyoung_comment.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제성공'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)