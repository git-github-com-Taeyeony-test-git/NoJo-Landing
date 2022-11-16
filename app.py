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
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.index_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/index/comment", methods=["GET"])
def index_comment_get():

    comment_list = list(db.index_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


# asher api
@app.route("/api/asher/comment", methods=["POST"])
def asher_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.asher_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/asher/comment", methods=["GET"])
def asher_comment_get():

    comment_list = list(db.asher_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


# bin api
@app.route("/api/bin/comment", methods=["POST"])
def bin_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.bin_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/bin/comment", methods=["GET"])
def bin_comment_get():
    
    comment_list = list(db.bin_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


# JungMin api
@app.route("/api/JungMin/comment", methods=["POST"])
def jungMin_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.JungMin_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/JungMin/comment", methods=["GET"])
def jungmin_comment_get():
    
    comment_list = list(db.JungMin_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


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

@app.route("/api/JungMin/comment", methods=["GET"])
def Taeyeon_comment_get():
    
    comment_list = list(db.Taeyeon_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

# jiyoung api
@app.route("/api/jiyoung/comment", methods=["POST"])
def jiyoung_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.jiyoung_comment.insert_one(doc)

    return jsonify({'msg': '등록완료'})

@app.route("/api/jiyoung/comment", methods=["GET"])
def jiyoung_comment_get():
    
    comment_list = list(db.jiyoung_comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)