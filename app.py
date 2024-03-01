from flask import Flask, render_template

app = Flask(__name__)
STATS = [
    {'sno':1, 'user':"SK",'steps':900},
    {'sno':12, 'user':"SK",'steps':900},
    {'sno':13, 'user':"SsK",'steps':1900},
    {'sno':123, 'user':"SK",'steps':900}
    ]
# @app.route("/")
# def helloworld():
#     return "hlwef"

@app.route("/")
def hello():
    return render_template('home.html',
                           stats = STATS)


if __name__ == '__main__':
    app.run(debug=True)