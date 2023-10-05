import os

from flask import Flask, render_template, request, flash, redirect, url_for
import requests

app = Flask(__name__)
# Dev
# app.secret_key = 'Friends'

# Prod
app.secret_key = os.environ.get('SECRET_KEY')
backend_base_url = os.environ.get('BACKEND_URL', 'http://backend:5000')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_todo', methods=['POST'])
def create_todo():
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'due_date': request.form['due_date']
    }

    response = requests.post(f'{backend_base_url}/todo', json=data)

    if response.status_code == 200:
        flash('To-do item created successfully!', 'success')
    else:
        flash('Error creating to-do item', 'error')

    return redirect(url_for('index'))


@app.route('/todos')
def list_todos():
    response = requests.get(f'{backend_base_url}/todos')
    todos = response.json() if response.status_code == 200 else []

    return render_template('todos.html', todos=todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
