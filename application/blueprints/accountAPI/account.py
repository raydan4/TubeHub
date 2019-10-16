from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

account = Blueprint('account', __name__, template_folder='templates')

@account.route('/')
def show_account():
    try:
        return render_template('/account/account.html')
    except TemplateNotFound:
        abort(404)

@account.route('/signin')
def show_siginin():
    try:
        return render_template('/account/signin.html')
    except TemplateNotFound:
        abort(404)

@account.route('/signup')
def show_signup():
    try:
        return render_template('/account/signup.html')
    except TemplateNotFound:
        abort(404)

@account.route('/logout')
def show_logout():
    try:
        return render_template('account/logout.html')
    except TemplateNotFound:
        abort(404)

@account.route('/manage')
def show_manage():
    try:
        return render_template('account/manage/manage.html')
    except TemplateNotFound:
        abort(404)

@account.route('/manage/update')
def show_update():
    try:
        return render_template('account/manage/update.html')
    except TemplateNotFound:
        abort(404)

@account.route('/manage/delete')
def show_delete():
    try:
        return render_template('account/manage/delete.html')
    except TemplateNotFound:
        abort(404)
