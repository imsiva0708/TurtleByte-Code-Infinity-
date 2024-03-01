from flask import Flask, render_template, jsonify ,request
from database import result_as_dict

STATS = result_as_dict
PROGRESS = 80
TOP = 10
SECOND = 65
app = Flask(__name__)

@app.route("/login-register")
def login():
    return render_template('index.html')

@app.route("/dashboard/apply")
def helloworld():
    data = request.args
    return jsonify(data)

@app.route("/")
def hello():
    return render_template('home.html',
                           stats = STATS,
                           top = TOP,
                           second = SECOND,
                           progress = PROGRESS)


if __name__ == '__main__':
    app.run(debug=True)