from app import app
from flask import render_template


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
