from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

video = Blueprint('video', __name__, template_folder='templates', static_folder='static')

@video.route('/upload')
def show_upload():
    try:
        return render_template('/video/upload.html')
    except TemplateNotFound:
        abort(404)

@video.route('/delete')
def show_delete():
    try:
        return render_template('/video/delete.html')
    except TemplateNotFound:
        abort(404)

@video.route('/watch')
def show_watch():
    try:
        title = 'nice'
        source = 'static/videos/classic.mp4'
        filetype = 'video/mp4'
        description = 'sad'
        return render_template('/video/watch.html', title=title, source=source, filetype=filetype)
    except TemplateNotFound:
        abort(404)


