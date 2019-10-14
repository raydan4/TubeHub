from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

videos = Blueprint('videos', __name__, template_folder='templates')

@videos.route('/upload')
def show_upload():
    try:
        return render_template('/videos/upload')
    except TemplateNotFound:
        abort(404)

@videos.route('/delete')
def show_delete():
    try:
        return render_template('/videos/delete')
    except TemplateNotFound:
        abort(404)

@videos.route('/watch')
def show_watch():
    try:
        return render_template('/videos/watch')
    except TemplateNotFound:
        abort(404)


