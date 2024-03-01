from flask import Flask, render_template
from database import result_as_dict

STATS = result_as_dict
PROGRESS = 80
TOP = 10
SECOND = 65
app = Flask(__name__)

# @app.route("/")
# def helloworld():
#     return "hlwef"

@app.route("/")
def hello():
    return render_template('home.html',
                           stats = STATS,
                           top = TOP,
                           second = SECOND,
                           progress = PROGRESS)


if __name__ == '__main__':
    app.run(debug=True)