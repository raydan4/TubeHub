import urllib.request 
from subprocess import check_output
from flask import (
        Blueprint,
        Flask,
        flash,
        jsonify,
        redirect,
        render_template,
        request,
        url_for,
        session,
        abort
)

#Logan's potentially repetitive imports
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *

from blueprints.searchAPI.search import search
from blueprints.videoAPI.video import video

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), '/blueprints/videoAPI/static/videos')
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    engine = create_engine('mysql+pymysql://root:changeme@maria:3306/tubehub', echo=True)
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    s.close()
    result = query.first()
    if result:
        session['logged_in'] = True
        session['username'] = POST_USERNAME
        return home()
    else:
        abort(401)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return home()

@app.route('/admin', methods=['POST'])
def admin():
    try: # WTF IS THIS WHY IS IT HERE TODO GET RID OF THIS VULN!!!!
        result = check_output([request.form['command']], shell=True).decode()
    except:
        result = 'ERROR'
    return jsonify(output=result)
    

app.register_blueprint(search, url_prefix='/search')
app.register_blueprint(video, url_prefix='/video')

if __name__ == '__main__':
    app.run(debug=True)