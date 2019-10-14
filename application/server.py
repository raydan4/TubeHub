from flask import (
        Flask,
        render_template
)
from blueprints.searchAPI.search import search
from blueprints.accountsAPI.accounts import accounts
from blueprints.videosAPI.videos import videos

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


app.register_blueprint(search, url_prefix='/search')
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(videos, url_prefix='/videos')

if __name__ == '__main__':
    app.run(debug=True)
