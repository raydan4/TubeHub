from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

accounts = Blueprint('accounts', __name__, template_folder='templates')

@accounts.route('/signin')
def show_siginin():
    try:
        return render_template('/accounts/signin')
    except TemplateNotFound:
        abort(404)

@accounts.route('/signup')
def show_signup():
    try:
        return render_template('/accounts/signup')
    except TemplateNotFound:
        abort(404)

@accounts.route('/logout')
def show_logout():
    try:
        return render_template('accounts/logout')
    except TemplateNotFound:
        abort(404)

@accounts.route('/update')
def show_upate():
    try:
        return render_template('accounts/update')
    except TemplateNotFound:
        abort(404)

@accounts.route('/delete')
def show_delete():
    try:
        return render_template('accounts/delete')
    except TemplateNotFound:
        abort(404)
