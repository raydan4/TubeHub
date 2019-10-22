from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

search = Blueprint('search', __name__, template_folder='templates')

@search.route('/')
def show_search():
    try:
        return render_template('/search/index.html')
    except TemplateNotFound:
        abort(404)

@search.route('/results')
def show_results():
    try:
        return render_template('/search/results.html')
    except TemplateNotFound:
        abort(404)
