from flask import Blueprint, render_template, abort, request, redirect, flash, session
from jinja2 import TemplateNotFound
from requests import get
from hashlib import sha3_256
import pymysql.cursors

video = Blueprint('video', __name__, template_folder='templates', static_folder='static')

VIDEO_DIR = 'static/videos/'

@video.route('/upload', methods=['GET', 'POST'])
def show_upload():
    if request.method == 'POST':
        # Get parameters from request
        sid = request.form.get('sessionid')
        userid = request.form.get('userid')
        title = request.form.get('title')
        description = request.form.get('description')
        filetype = request.form.get('filetype')

        ## Validate form input
        # Logged in
#        if not session.get(logged_in):
#            abort(401)
        # Video is Present
        video = request.files.get('video')
        if video and video.filename:
            location = os.path.join(VIDEO_DIR, sha3_256(video.read().hexdigest()))
            # Save video file to server (no validation lol all in same directory)
            video.save(location)
        else:
            # Get file from link
            link = request.form.get('link')
            if not link:
                flash('error: no file found to upload')
                abort(400)
            video = get(link)
            location = os.path.join(VIDEO_DIR, sha3_256(video.content).hexdigest())
            with open(location, 'wb') as f:
                f.write(video.content)

        
        # Connect to database
        connection = pymysql.connect(host='maria',
                             user='root',
                             password='changeme',
                             db='tubehub',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

        # Add video info to database
        try:
            with connection.cursor() as cur:
                sql = "INSERT INTO `video` (`title`, `userid`, `description`, `location`, `filetype`) VALUES (%s, %s, %s, %s, %s)"
                cur.execute(sql, (title, userid, description, location, filetype))
                connection.commit()
        finally:
            connection.close()
        return redirect('/upload')

    if request.method == 'GET':
        try:
            return render_template('/video/upload.html')
        except TemplateNotFound:
            abort(404)

@video.route('/delete', methods=['POST'])
def show_delete():
    # Check logged in
#    if not session.get('logged_in')
#        abort(403)

    # Remove file
    location = request.form.get('location')
    os.remove(location)
        
    # Connect to database
    connection = pymysql.connect(host='maria',
                         user='root',
                         password='changeme',
                         db='tubehub',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
        
    # Remove database entry
    with connection.cursor() as cur:
        pass

@video.route('/watch')
def show_watch():
    try:
        source = request.form.get('location')
        title = request.form['title']
        filetype = request.form['filetype']
        description = reqhest.form['description']
        return render_template('/video/watch.html', title=title, source=source, filetype=filetype, description=description)
    except TemplateNotFound:
        abort(404)


