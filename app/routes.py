from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'bob'}
    todo_list = [
        {
            'item': 'laundry',
            'completed': False,
            'Description': 'do laundry'
        },
        {
            'item': 'dishes',
            'completed': False,
            'Description': 'wash dishes'
        }
    ]
    return render_template('index.html', title="home", user=user, todo_list=todo_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='sign in', form=form)
