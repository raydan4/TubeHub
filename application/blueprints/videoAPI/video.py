from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

video = Blueprint('video', __name__, template_folder='templates', static_folder='static')

@video.route('/upload', methods=['GET', 'POST'])
def show_upload():
    if request.method == 'POST':
        # Get parameters from request
        sid = request.form['sessionid']
        userid = request.form['urserid']
        name = request.form['name']
        description = request.form['description']
        location = request.form['location']
        filetype = request.form['filetype']

        ## Validate form input
        # Logged in
        if not sessionid_isvalid(sid):
            abort(403)
        # Video is Present
        video = request.files.get('video')
        if not video or not video.filename:
            abort(400)
        
        # Connect to database
        connection = pymysql.connect(host='maria',
                             user='root',
                             password='changeme',
                             db='tubehub',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        cur = connection.cursor()


        # Add video info to database
        sql = "INSERT INTO `video` (`name`, `userid`, `description`, `location`, `filetype`) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (name, userid, description, location, filetype))
        connection.commit()

        # Save video file to server (no validation lol all in same directory)
        video.save(os.path.join('static/videos/', video.filename))

        return redirect('/upload')
    if request.method == 'GET':
        try:
            return render_template('/video/upload.html')
        except TemplateNotFound:
            abort(404)

@video.route('/delete', methods=['POST'])
def show_delete():
    if request.method == 'POST':
        
        # Remove file
        location = request.form['location']
        os.remove(location)
        
        # Connect to database
        connection = pymysql.connect(host='maria',
                             user='root',
                             password='changeme',
                             db='tubehub',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        cur = connection.cursor()
        
        # Remove database entry

    if request.method == 'GEt':
        try:
            return render_template('/video/delete.html')
        except TemplateNotFound:
            abort(404)

@video.route('/watch')
def show_watch():
    try:
        title = request.form['name']
        source = request.form['location']
        filetype = request.form['filetype']
        description = reqhest.form['description']
        return render_template('/video/watch.html', title=title, source=source, filetype=filetype, description=description)
    except TemplateNotFound:
        abort(404)


