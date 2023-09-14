from pathlib import PurePath, Path


from flask import Flask, render_template, request, abort, redirect, url_for, flash, make_response
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask('__name__')


@app.route('/index/')
def index():
    context = {
        'title': 'seminar 2'
    }
    return render_template('base.html', **context)


@app.route('/task9', methods=['GET', 'POST'])
def task9_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect('/task9_welcome'))
        response.set_cookie('user_name', name)
        response.set_cookie('user_email', email)
        return response
    return render_template('task9_form.html', title='Task 9 - FORM')

@app.route('/task9_welcome/')
def task9_welcome():
    context = {
        'title': 'Task 9',
        'name': request.cookies.get('user_name')
    }
    return render_template('task9_welcome.html', **context)

@app.route('/task9_logout/')
def task9_logout():
    response = redirect('/task9')
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response

if __name__ == '__main__':
    app.run(debug=True)