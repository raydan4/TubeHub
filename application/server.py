import urllib.request 
import pymysql
from pymysql import cursors
from datetime import datetime
from flask import (
        Blueprint,
        Flask,
        render_template,
        request,
        redirect,
        flash
)

from blueprints.searchAPI.search import search
from blueprints.accountAPI.account import account
from blueprints.videoAPI.video import video

app = Flask(__name__)

connection = pymysql.connect(host='maria',
                             user='root',
                             password='changeme',
                             db='tubehub',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cur = connection.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        date = datetime.now()
 
        sql = "INSERT INTO `users` (`username`, `password`, `birthdate`, `email`, `sessionid`) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (username, password, date, "example@email.com", "jkfal13k3jfdq"))
        connection.commit()

        return redirect("/login")
    if request.method == 'GET':
        return render_template("signup.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        return redirect("/login")
    if request.method == 'GET':
        return render_template("signin.html")


@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return redirect("/login")
    if request.method == 'GET':
        return render_template("home.html")

app.register_blueprint(search, url_prefix='/search')
app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(video, url_prefix='/video')

if __name__ == '__main__':
    app.run(debug=True)
