from flask import Flask, render_template, redirect ,request
from database import load_from_db, add_to_db

STATS = load_from_db()
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('homepage.html')


@app.route("/dashboard/apply")
def helloworld():
    data = request.args
    # add_to_db(data,Name)
    return render_template('tmp.html')

@app.route("/login-register")
def login():
    return render_template("index.html")

@app.route("/dashboard" , methods = ['post'])
def hello():
    account_dict = request.form.to_dict()
    global Name
    Name= account_dict['name']
    return render_template('home.html',
                           stats = STATS
                           )

@app.route("/workout.html")
def work():
    return render_template("workout.html")


if __name__ == '__main__':
    app.run(debug=True)