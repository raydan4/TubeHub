from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

video = Blueprint('video', __name__, template_folder='templates')

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
        return render_template('/video/watch.html')
    except TemplateNotFound:
        abort(404)


